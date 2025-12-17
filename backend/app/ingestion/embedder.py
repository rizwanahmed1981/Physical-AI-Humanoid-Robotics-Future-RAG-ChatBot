"""
Embedder for RAG Ingestion Pipeline
Handles generation of vector embeddings for content chunks.
"""

import os
import logging
from typing import List, Dict, Union
from openai import OpenAI
from openai.types import CreateEmbeddingResponse
import time
from tenacity import retry, stop_after_attempt, wait_exponential

logger = logging.getLogger(__name__)

class Embedder:
    """Generate vector embeddings for text content."""

    def __init__(self, model: str = "text-embedding-3-small"):
        """
        Initialize embedder with OpenAI client.

        Args:
            model: OpenAI embedding model to use
        """
        # Initialize OpenAI client
        api_key = os.getenv('OPENAI_API_KEY')
        if not api_key:
            raise ValueError("OPENAI_API_KEY environment variable is required")

        self.client = OpenAI(api_key=api_key)
        self.model = model
        self.rate_limit_delay = 0.1  # Delay between requests to avoid rate limiting

    @retry(stop=stop_after_attempt(3), wait=wait_exponential(multiplier=1, max=10))
    def generate_embedding(self, text: str) -> List[float]:
        """
        Generate embedding for a single text.

        Args:
            text: Text to embed

        Returns:
            List of embedding values
        """
        try:
            # Call OpenAI API to generate embedding
            response: CreateEmbeddingResponse = self.client.embeddings.create(
                model=self.model,
                input=text
            )

            # Extract the embedding vector
            embedding = response.data[0].embedding

            logger.debug(f"Generated embedding with {len(embedding)} dimensions")
            return embedding

        except Exception as e:
            logger.error(f"Error generating embedding: {str(e)}")
            raise

    def generate_embeddings_batch(self, texts: List[str]) -> List[List[float]]:
        """
        Generate embeddings for a batch of texts.

        Args:
            texts: List of texts to embed

        Returns:
            List of embedding vectors
        """
        embeddings = []

        # Process in batches to respect rate limits
        batch_size = 10  # OpenAI allows up to 2048 embeddings per request

        for i in range(0, len(texts), batch_size):
            batch = texts[i:i + batch_size]

            try:
                # Generate embeddings for the batch
                response: CreateEmbeddingResponse = self.client.embeddings.create(
                    model=self.model,
                    input=batch
                )

                # Extract embeddings
                batch_embeddings = [item.embedding for item in response.data]
                embeddings.extend(batch_embeddings)

                # Respect rate limits
                time.sleep(self.rate_limit_delay)

            except Exception as e:
                logger.error(f"Error generating batch embeddings: {str(e)}")
                # For failed batches, we could retry or skip, but for simplicity we'll raise
                raise

        return embeddings

    def generate_embeddings_for_chunks(self, chunks: List[Dict[str, str]]) -> List[Dict[str, Union[str, List[float]]]]:
        """
        Generate embeddings for a list of chunks.

        Args:
            chunks: List of chunk dictionaries

        Returns:
            List of chunk dictionaries with added embeddings
        """
        # Prepare texts for embedding
        texts_to_embed = [chunk['content'] for chunk in chunks]

        # Generate embeddings
        embeddings = self.generate_embeddings_batch(texts_to_embed)

        # Add embeddings back to chunks
        for i, chunk in enumerate(chunks):
            chunk['embedding'] = embeddings[i]
            chunk['embedding_version'] = self.model

        return chunks