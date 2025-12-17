"""
Data models for retrieval module
"""

from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class RetrievedChunk(BaseModel):
    """Represents a chunk retrieved from the vector database"""

    chunk_id: str
    document_id: str
    source_file: str
    section_title: str
    content: str
    chunk_position: tuple  # (start, end)
    chunk_type: str
    similarity_score: float
    created_at: datetime
    embedding_version: str

class QueryRequest(BaseModel):
    """Request model for RAG query"""

    query: str
    top_k: int = 5
    collection_name: str = "textbook_content"
    min_similarity: float = 0.0

class QueryResponse(BaseModel):
    """Response model for RAG query"""

    query: str
    top_k: int
    retrieved_chunks: List[RetrievedChunk]
    total_retrieved: int
    collection_name: str
    timestamp: datetime