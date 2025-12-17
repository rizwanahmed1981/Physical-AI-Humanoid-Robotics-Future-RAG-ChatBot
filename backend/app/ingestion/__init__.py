"""
RAG Ingestion Pipeline Package
"""

__version__ = "0.1.0"
__author__ = "Physical-AI-Humanoid-Robotics-Future Team"

# Import main components for easy access
from .parser import MarkdownParser
from .chunker import Chunker
from .embedder import Embedder
from .qdrant_client import QdrantClient
from .main import ingest_documents

__all__ = [
    "MarkdownParser",
    "Chunker",
    "Embedder",
    "QdrantClient",
    "ingest_documents"
]