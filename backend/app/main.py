from fastapi import APIRouter
from app.retrieval.retrieval import RetrievalService
from app.api.retrieve import router as retrieve_router


router = APIRouter()
retriever = RetrievalService()

app.include_router(
    retrieve_router,
    prefix="/api/v1",
    tags=["retrieval"]
)

@router.post("/retrieve")
def retrieve(query: str, top_k: int = 5):
    results = retriever.retrieve(query, top_k)
    return {
        "query": query,
        "retrieved_count": len(results),
        "results": results
    }
