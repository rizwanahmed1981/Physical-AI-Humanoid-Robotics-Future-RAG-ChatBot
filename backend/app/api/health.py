from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class HealthResponse(BaseModel):
    status: str
    version: str

@router.get("/health", response_model=HealthResponse)
async def health_check():
    """
    Health check endpoint to verify API is running
    """
    return HealthResponse(status="healthy", version="1.0.0")

@router.get("/ready")
async def readiness_check():
    """
    Readiness check endpoint
    """
    # Placeholder - in a real implementation, this would check database connections, etc.
    return {"status": "ready"}