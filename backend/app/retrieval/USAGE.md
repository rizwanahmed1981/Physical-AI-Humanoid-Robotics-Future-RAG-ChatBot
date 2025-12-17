# RAG Retrieval API Usage Examples

## Running the API Server

```bash
cd /path/to/project
export OPENAI_API_KEY="your-openai-api-key"
export QDRANT_CLUSTER_ID="92277f56-d324-4ebd-9404-1dfa6ac7c943"  # or QDRANT_HOST
python3 -m backend.app.retrieval.main
```

## API Endpoints

### Root Endpoint
```
GET /
```
Health check to verify the API is running.

### Retrieve Endpoint
```
POST /rag/retrieve
```
Retrieve relevant chunks from the vector database based on user queries.

**Request Body:**
```json
{
  "query": "What are the foundations of physical AI and humanoid robotics?",
  "top_k": 5,
  "collection_name": "textbook_content",
  "min_similarity": 0.5
}
```

**Parameters:**
- `query`: (required) The user query string to search for relevant content
- `top_k`: (optional, default: 5) Number of top results to return (1-100)
- `collection_name`: (optional, default: "textbook_content") Name of the Qdrant collection to search
- `min_similarity`: (optional, default: 0.0) Minimum similarity threshold for results

**Response:**
```json
{
  "query": "What are the foundations of physical AI and humanoid robotics?",
  "top_k": 5,
  "retrieved_chunks": [
    {
      "chunk_id": "chunk-123",
      "document_id": "doc-456",
      "source_file": "chapter1.md",
      "section_title": "Introduction to Physical AI",
      "content": "Physical AI combines robotics, machine learning, and embodied intelligence...",
      "chunk_position": [0, 250],
      "chunk_type": "paragraph",
      "similarity_score": 0.876,
      "created_at": "2025-01-15T10:30:00Z",
      "embedding_version": "v1"
    }
  ],
  "total_retrieved": 1,
  "collection_name": "textbook_content",
  "timestamp": "2025-01-15T10:30:00Z"
}
```

## Environment Variables

Required:
- `OPENAI_API_KEY`: Your OpenAI API key for generating embeddings
- Either `QDRANT_HOST` or `QDRANT_CLUSTER_ID`: Connection details for Qdrant database

Optional:
- `RETRIEVAL_API_HOST`: Host for the API server (default: 0.0.0.0)
- `RETRIEVAL_API_PORT`: Port for the API server (default: 8001)

## Example cURL Request

```bash
curl -X POST http://localhost:8001/rag/retrieve \
  -H "Content-Type: application/json" \
  -d '{
    "query": "Explain the basics of humanoid robotics",
    "top_k": 3,
    "collection_name": "textbook_content",
    "min_similarity": 0.6
  }'
```

## Python Client Example

```python
import requests

url = "http://localhost:8001/rag/retrieve"
payload = {
    "query": "What are the key components of a humanoid robot?",
    "top_k": 5,
    "collection_name": "textbook_content",
    "min_similarity": 0.5
}

response = requests.post(url, json=payload)
data = response.json()

for chunk in data['retrieved_chunks']:
    print(f"Source: {chunk['source_file']}")
    print(f"Section: {chunk['section_title']}")
    print(f"Content: {chunk['content'][:200]}...")
    print(f"Similarity: {chunk['similarity_score']}")
    print("---")
```