"""
Simple test for the RAG retrieval API endpoint without pytest
"""

from fastapi.testclient import TestClient
from backend.app.retrieval.main import app

def test_api_endpoints():
    """Test the API endpoints."""
    client = TestClient(app)

    # Test root endpoint
    response = client.get("/")
    print(f"Root endpoint status: {response.status_code}")
    print(f"Root endpoint response: {response.json()}")
    assert response.status_code == 200
    assert "message" in response.json()
    assert "RAG Retrieval API is running" in response.json()["message"]

    # Test retrieve endpoint exists (will fail due to missing env vars, but should not be 404)
    response = client.post(
        "/rag/retrieve",
        json={"query": "test query", "top_k": 3}
    )
    print(f"Retrieve endpoint status: {response.status_code}")
    # Should not be 404 (not found), could be 422 (validation error) or 500 (internal due to missing env vars)
    assert response.status_code != 404

    print("API endpoint tests passed!")

if __name__ == "__main__":
    test_api_endpoints()