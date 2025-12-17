"""
Main module for RAG retrieval API
Implements the FastAPI endpoints for the RAG system
"""

import logging
import os
from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional
import uvicorn

from .models import QueryRequest, QueryResponse
from .retriever import Retriever

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Create FastAPI app
app = FastAPI(
    title="RAG Retrieval API",
    description="API for retrieving relevant chunks from vector database based on user queries",
    version="0.1.0"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with specific origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize the retriever
retriever: Optional[Retriever] = None

def get_retriever():
    """Dependency function to get the retriever instance."""
    global retriever
    if retriever is None:
        try:
            retriever = Retriever()
            logger.info("Initialized RAG retriever")
        except Exception as e:
            logger.error(f"Failed to initialize retriever: {str(e)}")
            raise HTTPException(status_code=500, detail=f"Failed to initialize retriever: {str(e)}")
    return retriever

@app.get("/")
async def root():
    """Root endpoint for health check."""
    return {"message": "RAG Retrieval API is running", "status": "healthy"}

@app.post("/rag/retrieve", response_model=QueryResponse)
async def retrieve_chunks(query_request: QueryRequest, retriever: Retriever = Depends(get_retriever)):
    """
    Retrieve relevant chunks from the vector database based on the user query.

    Args:
        query_request: QueryRequest containing the query and retrieval parameters
        retriever: Retriever instance (injected via dependency)

    Returns:
        QueryResponse containing the retrieved chunks and metadata
    """
    try:
        logger.info(f"Processing retrieval request for query: {query_request.query[:50]}...")

        # Validate query length
        if not query_request.query or len(query_request.query.strip()) == 0:
            raise HTTPException(status_code=400, detail="Query cannot be empty")

        if len(query_request.query) > 1000:  # Arbitrary limit, can be adjusted
            raise HTTPException(status_code=400, detail="Query too long. Maximum 1000 characters allowed.")

        # Validate top_k parameter
        if query_request.top_k <= 0 or query_request.top_k > 100:  # Reasonable limits
            raise HTTPException(status_code=400, detail="top_k must be between 1 and 100")

        # Perform retrieval
        response = retriever.retrieve_chunks(query_request)

        logger.info(f"Successfully retrieved {response.total_retrieved} chunks for query")
        return response

    except HTTPException:
        # Re-raise HTTP exceptions as-is
        raise
    except Exception as e:
        logger.error(f"Error processing retrieval request: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Error processing retrieval request: {str(e)}")

@app.get("/health")
async def health_check(retriever: Retriever = Depends(get_retriever)):
    """Health check endpoint that also verifies retriever functionality."""
    try:
        # Test the retriever connection
        test_embedding = retriever._generate_query_embedding("test query")
        if not test_embedding or len(test_embedding) == 0:
            raise Exception("Could not generate test embedding")

        return {
            "status": "healthy",
            "retriever": "initialized",
            "openai_connection": "verified",
            "qdrant_connection": "verified"
        }
    except Exception as e:
        logger.error(f"Health check failed: {str(e)}")
        raise HTTPException(status_code=503, detail=f"Health check failed: {str(e)}")

def main():
    """Main function to run the API server."""
    # Check required environment variables
    required_env_vars = ['OPENAI_API_KEY', 'QDRANT_HOST']
    missing_vars = [var for var in required_env_vars if not os.getenv(var)]

    if missing_vars:
        logger.warning(f"Missing required environment variables: {missing_vars}")
        logger.info("Please set these environment variables before running the API")

    # Get host and port from environment or use defaults
    host = os.getenv('RETRIEVAL_API_HOST', '0.0.0.0')
    port = int(os.getenv('RETRIEVAL_API_PORT', '8001'))

    logger.info(f"Starting RAG Retrieval API on {host}:{port}")

    uvicorn.run(
        "backend.app.retrieval.main:app",
        host=host,
        port=port,
        reload=True,  # Disable in production
        log_level="info"
    )

if __name__ == "__main__":
    main()