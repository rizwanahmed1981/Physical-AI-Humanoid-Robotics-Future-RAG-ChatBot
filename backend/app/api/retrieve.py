from fastapi import APIRouter
from app.services.retrieval import RetrievalService

router = APIRouter()
retriever = RetrievalService()

@router.post("/retrieve")
def retrieve(payload: dict):
    query = payload.get("query")
    top_k = payload.get("top_k", 5)

    if not query:
        return {"error": "Query is required"}

    results = retriever.retrieve(query=query, top_k=top_k)

    return {
        "query": query,
        "retrieved_count": len(results),
        "results": results
    }
