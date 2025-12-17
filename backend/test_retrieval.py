"""
Test script for RAG retrieval functionality
"""

import asyncio
import os
from backend.app.retrieval.retriever import Retriever
from backend.app.retrieval.models import QueryRequest

def test_retrieval():
    """Test the retrieval functionality."""

    # Set up environment variables if not already set
    if not os.getenv('OPENAI_API_KEY'):
        # In a real scenario, you'd set this properly
        print("Please set OPENAI_API_KEY environment variable")
        return

    if not os.getenv('QDRANT_HOST') and not os.getenv('QDRANT_CLUSTER_ID'):
        # Set the cluster ID if available
        os.environ['QDRANT_CLUSTER_ID'] = '92277f56-d324-4ebd-9404-1dfa6ac7c943'

    try:
        # Initialize the retriever
        print("Initializing retriever...")
        retriever = Retriever()

        # Create a test query
        query_request = QueryRequest(
            query="What are the foundations of physical AI and humanoid robotics?",
            top_k=3,
            collection_name="textbook_content",
            min_similarity=0.5
        )

        print(f"Processing query: {query_request.query}")

        # Perform retrieval
        response = retriever.retrieve_chunks(query_request)

        print(f"Retrieved {response.total_retrieved} chunks:")
        for i, chunk in enumerate(response.retrieved_chunks):
            print(f"\nChunk {i+1}:")
            print(f"  Source: {chunk.source_file}")
            print(f"  Section: {chunk.section_title}")
            print(f"  Similarity: {chunk.similarity_score:.3f}")
            print(f"  Content preview: {chunk.content[:100]}...")

        print(f"\nTotal retrieved: {response.total_retrieved}")
        print(f"Query: {response.query}")

    except Exception as e:
        print(f"Error during retrieval test: {str(e)}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    test_retrieval()