"""
Retrieval Module for RAG System
Implements the retrieval and query pipeline for the RAG system
"""

__version__ = "0.1.0"
__author__ = "Physical-AI-Humanoid-Robotics-Future Team"

# Import main components for easy access
from .retriever import Retriever
from .models import QueryRequest, QueryResponse, RetrievedChunk
from .main import app

__all__ = [
    "Retriever",
    "QueryRequest",
    "QueryResponse",
    "RetrievedChunk",
    "app"
]