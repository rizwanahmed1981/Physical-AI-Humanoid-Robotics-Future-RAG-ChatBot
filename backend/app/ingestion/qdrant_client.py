"""
Qdrant Client for RAG Ingestion Pipeline
Handles interaction with Qdrant vector database.
"""

import os
import logging
from typing import List, Dict, Union, Optional
from qdrant_client import QdrantClient as QdrantClientImpl
from qdrant_client.models import VectorParams, Filter, FieldCondition, MatchValue, FilterSelector
from qdrant_client.http.models import PointStruct
import uuid
from datetime import datetime

logger = logging.getLogger(__name__)

class QdrantClient:
    """Client for interacting with Qdrant vector database."""

    def __init__(self, host: str = None, port: int = None, api_key: str = None):
        """
        Initialize Qdrant client.

        Args:
            host: Qdrant host address
            port: Qdrant port
            api_key: Qdrant API key (if required)
        """
        # Get configuration from environment variables
        self.host = host or os.getenv('QDRANT_HOST', 'localhost')
        self.port = port or int(os.getenv('QDRANT_PORT', '6333'))
        self.api_key = api_key or os.getenv('QDRANT_API_KEY')

        # Initialize Qdrant client
        try:
            if self.api_key:
                self.client = QdrantClientImpl(host=self.host, port=self.port, api_key=self.api_key)
            else:
                self.client = QdrantClientImpl(host=self.host, port=self.port)

            # Test connection
            self.client.health_check()
            logger.info("Successfully connected to Qdrant")

        except Exception as e:
            logger.error(f"Failed to connect to Qdrant: {str(e)}")
            raise

    def create_collection(self, collection_name: str, vector_size: int = 1536,
                         distance: str = "Cosine") -> bool:
        """
        Create a collection in Qdrant if it doesn't exist.

        Args:
            collection_name: Name of the collection
            vector_size: Size of the vector embeddings
            distance: Distance metric (Cosine, Euclid, etc.)

        Returns:
            True if collection was created or already existed
        """
        try:
            # Check if collection exists
            collections = self.client.get_collections()
            collection_names = [collection.name for collection in collections.collections]

            if collection_name in collection_names:
                logger.info(f"Collection '{collection_name}' already exists")
                return True

            # Create collection with specified parameters
            self.client.create_collection(
                collection_name=collection_name,
                vectors_config=VectorParams(size=vector_size, distance=distance)
            )

            logger.info(f"Created collection '{collection_name}' with {vector_size} dimensional vectors")
            return True

        except Exception as e:
            logger.error(f"Error creating collection '{collection_name}': {str(e)}")
            raise

    def upsert_points(self, collection_name: str, points: List[PointStruct]) -> bool:
        """
        Upsert points into Qdrant collection.

        Args:
            collection_name: Name of the collection
            points: List of PointStruct objects to upsert

        Returns:
            True if successful
        """
        try:
            # Upsert points
            self.client.upsert(
                collection_name=collection_name,
                points=points
            )

            logger.info(f"Upserted {len(points)} points into collection '{collection_name}'")
            return True

        except Exception as e:
            logger.error(f"Error upserting points: {str(e)}")
            raise

    def create_point_from_chunk(self, chunk: Dict[str, Union[str, List[float]]]) -> PointStruct:
        """
        Create a PointStruct from a chunk dictionary.

        Args:
            chunk: Chunk dictionary with content and metadata

        Returns:
            PointStruct for Qdrant
        """
        # Prepare payload with metadata
        payload = {
            'chunk_id': chunk.get('chunk_id'),
            'document_id': chunk.get('document_id'),
            'source_file': chunk.get('source_file'),
            'section_title': chunk.get('section_title'),
            'chunk_position': chunk.get('chunk_position'),
            'chunk_type': chunk.get('chunk_type', 'paragraph'),
            'created_at': chunk.get('created_at', datetime.utcnow().isoformat()),
            'embedding_version': chunk.get('embedding_version', 'unknown')
        }

        # Add any additional metadata
        for key, value in chunk.items():
            if key not in ['content', 'embedding']:
                payload[key] = value

        # Create PointStruct
        point = PointStruct(
            id=chunk.get('chunk_id', str(uuid.uuid4())),
            vector=chunk.get('embedding', []),
            payload=payload
        )

        return point

    def upsert_chunks(self, collection_name: str, chunks: List[Dict[str, Union[str, List[float]]]]) -> int:
        """
        Upsert chunks into Qdrant collection.

        Args:
            collection_name: Name of the collection
            chunks: List of chunk dictionaries

        Returns:
            Number of chunks upserted
        """
        try:
            # Create collection if it doesn't exist
            self.create_collection(collection_name)

            # Convert chunks to PointStructs
            points = []
            for chunk in chunks:
                point = self.create_point_from_chunk(chunk)
                points.append(point)

            # Upsert all points
            self.upsert_points(collection_name, points)

            logger.info(f"Successfully upserted {len(points)} chunks into '{collection_name}'")
            return len(points)

        except Exception as e:
            logger.error(f"Error upserting chunks: {str(e)}")
            raise

    def get_collection_info(self, collection_name: str) -> Dict:
        """
        Get information about a collection.

        Args:
            collection_name: Name of the collection

        Returns:
            Collection information
        """
        try:
            info = self.client.get_collection(collection_name)
            return {
                'name': info.name,
                'status': info.status,
                'vectors_count': info.vectors_count,
                'indexed_vectors_count': info.indexed_vectors_count,
                'points_count': info.points_count,
                'config': info.config
            }
        except Exception as e:
            logger.error(f"Error getting collection info: {str(e)}")
            raise