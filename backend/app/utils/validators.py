"""
Validation utilities for RAG ingestion pipeline
"""

import re
from typing import Dict, Any, List
import logging

logger = logging.getLogger(__name__)

def validate_chunk_content(chunk: Dict[str, Any]) -> bool:
    """
    Validate that a chunk has required fields and valid content.

    Args:
        chunk: Chunk dictionary to validate

    Returns:
        True if valid, False otherwise
    """
    required_fields = ['content', 'chunk_id', 'document_id', 'source_file']

    # Check required fields
    for field in required_fields:
        if field not in chunk or not chunk[field]:
            logger.warning(f"Missing required field '{field}' in chunk")
            return False

    # Validate content length
    if len(chunk['content']) < 10:  # Minimum reasonable content length
        logger.warning(f"Chunk content too short: {len(chunk['content'])} characters")
        return False

    # Validate chunk ID format
    if not re.match(r'^chunk_[a-f0-9]{8}$', chunk['chunk_id']):
        logger.warning(f"Invalid chunk ID format: {chunk['chunk_id']}")
        return False

    # Validate document ID format
    if not re.match(r'^doc_[a-f0-9]{8}$', chunk['document_id']):
        logger.warning(f"Invalid document ID format: {chunk['document_id']}")
        return False

    return True

def validate_embedding(embedding: List[float]) -> bool:
    """
    Validate that an embedding has reasonable properties.

    Args:
        embedding: List of embedding values

    Returns:
        True if valid, False otherwise
    """
    if not isinstance(embedding, list):
        logger.warning("Embedding is not a list")
        return False

    if len(embedding) == 0:
        logger.warning("Embedding is empty")
        return False

    # Check that all values are numbers
    for value in embedding:
        if not isinstance(value, (int, float)):
            logger.warning(f"Non-numeric value in embedding: {value}")
            return False

    return True

def validate_qdrant_point(point_data: Dict[str, Any]) -> bool:
    """
    Validate that Qdrant point data has required fields.

    Args:
        point_data: Qdrant point data dictionary

    Returns:
        True if valid, False otherwise
    """
    required_fields = ['chunk_id', 'document_id', 'source_file', 'embedding']

    for field in required_fields:
        if field not in point_data:
            logger.warning(f"Missing required field '{field}' in point data")
            return False

    # Validate embedding
    if not validate_embedding(point_data['embedding']):
        logger.warning("Invalid embedding in point data")
        return False

    return True