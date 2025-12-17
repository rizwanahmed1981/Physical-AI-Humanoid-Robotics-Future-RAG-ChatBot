"""
Retriever module for RAG system
Handles vector search and retrieval from Qdrant database
"""

import logging
from typing import List, Dict, Any
from openai import OpenAI
from qdrant_client import QdrantClient as QdrantClientImpl
from ..ingestion.qdrant_client import QdrantClient
from .models import RetrievedChunk, QueryRequest, QueryResponse
import os
from datetime import datetime

logger = logging.getLogger(__name__)

class Retriever:
    """Handles retrieval of relevant chunks from vector database based on user queries."""

    def __init__(self):
        """Initialize the retriever with OpenAI client and Qdrant client."""
        # Initialize OpenAI client
        openai_api_key = os.getenv('OPENAI_API_KEY')
        if not openai_api_key:
            raise ValueError("OPENAI_API_KEY environment variable is required")

        self.openai_client = OpenAI(api_key=openai_api_key)

        # Initialize Qdrant client
        self.qdrant_client = QdrantClient()

    def _generate_query_embedding(self, query: str) -> List[float]:
        """
        Generate embedding for the query using OpenAI.

        Args:
            query: User query string

        Returns:
            List of floats representing the embedding vector
        """
        try:
            response = self.openai_client.embeddings.create(
                input=query,
                model="text-embedding-ada-002"  # Using ada-002 as it's efficient and effective
            )

            embedding = response.data[0].embedding
            logger.debug(f"Generated embedding with {len(embedding)} dimensions for query: {query[:50]}...")
            return embedding

        except Exception as e:
            logger.error(f"Error generating query embedding: {str(e)}")
            raise

    def retrieve_chunks(self, query_request: QueryRequest) -> QueryResponse:
        """
        Retrieve relevant chunks from the vector database based on the query.

        Args:
            query_request: QueryRequest containing the query and parameters

        Returns:
            QueryResponse containing the retrieved chunks and metadata
        """
        try:
            # Generate embedding for the query
            query_embedding = self._generate_query_embedding(query_request.query)

            # Perform vector search in Qdrant
            search_results = self.qdrant_client.client.search(
                collection_name=query_request.collection_name,
                query_vector=query_embedding,
                limit=query_request.top_k,
                score_threshold=query_request.min_similarity
            )

            # Convert search results to RetrievedChunk objects
            retrieved_chunks = []
            for result in search_results:
                chunk_data = result.payload

                # Create RetrievedChunk object from search result
                retrieved_chunk = RetrievedChunk(
                    chunk_id=chunk_data.get('chunk_id', ''),
                    document_id=chunk_data.get('document_id', ''),
                    source_file=chunk_data.get('source_file', ''),
                    section_title=chunk_data.get('section_title', ''),
                    content=result.payload.get('content', '') if hasattr(result, 'payload') and result.payload else '',
                    chunk_position=chunk_data.get('chunk_position', (0, 0)),
                    chunk_type=chunk_data.get('chunk_type', 'paragraph'),
                    similarity_score=result.score,
                    created_at=datetime.fromisoformat(chunk_data.get('created_at', datetime.utcnow().isoformat())),
                    embedding_version=chunk_data.get('embedding_version', 'unknown')
                )

                retrieved_chunks.append(retrieved_chunk)

            # Create and return QueryResponse
            response = QueryResponse(
                query=query_request.query,
                top_k=query_request.top_k,
                retrieved_chunks=retrieved_chunks,
                total_retrieved=len(retrieved_chunks),
                collection_name=query_request.collection_name,
                timestamp=datetime.utcnow()
            )

            logger.info(f"Retrieved {len(retrieved_chunks)} chunks for query: {query_request.query[:50]}...")
            return response

        except Exception as e:
            logger.error(f"Error retrieving chunks: {str(e)}")
            raise

    def search_by_content(self, query: str, top_k: int = 5, collection_name: str = "textbook_content") -> List[Dict[str, Any]]:
        """
        Alternative search method that returns raw results for more flexible processing.

        Args:
            query: Search query string
            top_k: Number of top results to return
            collection_name: Name of the collection to search in

        Returns:
            List of dictionaries containing search results
        """
        try:
            query_embedding = self._generate_query_embedding(query)

            search_results = self.qdrant_client.client.search(
                collection_name=collection_name,
                query_vector=query_embedding,
                limit=top_k
            )

            results = []
            for result in search_results:
                result_dict = {
                    'payload': result.payload,
                    'score': result.score,
                    'id': result.id
                }
                results.append(result_dict)

            return results

        except Exception as e:
            logger.error(f"Error in content search: {str(e)}")
            raise