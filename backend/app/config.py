import os
from typing import Optional

class Config:
    """
    Configuration class for the Physical-AI-Humanoid-Robotics RAG application
    """

    # Application settings
    APP_NAME = os.getenv("APP_NAME", "Physical-AI-Humanoid-Robotics-RAG")
    APP_VERSION = os.getenv("APP_VERSION", "1.0.0")
    DEBUG = os.getenv("DEBUG", "False").lower() == "true"

    # API settings
    API_V1_STR = "/api/v1"
    PROJECT_NAME = os.getenv("PROJECT_NAME", "Physical-AI-Humanoid-Robotics RAG API")

    # Database settings (placeholder)
    DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./rag_database.db")

    # Embedding settings
    EMBEDDING_MODEL = os.getenv("EMBEDDING_MODEL", "text-embedding-ada-002")
    EMBEDDING_DIMENSION = int(os.getenv("EMBEDDING_DIMENSION", "1536"))

    # Generation settings
    LLM_MODEL = os.getenv("LLM_MODEL", "gpt-3.5-turbo")
    MAX_TOKENS = int(os.getenv("MAX_TOKENS", "1000"))
    TEMPERATURE = float(os.getenv("TEMPERATURE", "0.7"))

    # Content settings
    TEXTBOOK_PATH = os.getenv("TEXTBOOK_PATH", "./textbook_content/")
    CHUNK_SIZE = int(os.getenv("CHUNK_SIZE", "1000"))
    CHUNK_OVERLAP = int(os.getenv("CHUNK_OVERLAP", "200"))

    # Vector store settings
    VECTOR_STORE_PATH = os.getenv("VECTOR_STORE_PATH", "./vector_store/")

    # CORS settings
    BACKEND_CORS_ORIGINS = os.getenv("BACKEND_CORS_ORIGINS", "*").split(",")

# Create a config instance
config = Config()