"""
Simple test for the RAG retrieval API endpoint
"""

import pytest
from fastapi.testclient import TestClient
from backend.app.retrieval.main import app

def test_api_root():
    """Test the root endpoint."""
    client = TestClient(app)
    response = client.get("/")
    assert response.status_code == 200
    assert "message" in response.json()
    assert "RAG Retrieval API is running" in response.json()["message"]

def test_health_check():
    """Test the health check endpoint."""
    client = TestClient(app)
    response = client.get("/health")
    # This might fail if environment variables aren't set, but should return appropriate status
    assert response.status_code in [200, 503]  # 503 if health check fails due to missing env vars

def test_retrieve_endpoint_structure():
    """Test that the retrieve endpoint exists and returns appropriate error for missing data."""
    client = TestClient(app)
    response = client.post(
        "/rag/retrieve",
        json={"query": "test query"}
    )
    # Should return 422 (validation error) or 500 (internal error due to missing env vars) rather than 404 (not found)
    assert response.status_code in [422, 500, 400]

if __name__ == "__main__":
    test_api_root()
    test_health_check()
    test_retrieve_endpoint_structure()
    print("API tests passed!")