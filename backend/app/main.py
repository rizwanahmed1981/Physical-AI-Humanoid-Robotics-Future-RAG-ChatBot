from fastapi import FastAPI
from app.api.chat import router as chat_router
from app.api.health import router as health_router

app = FastAPI(
    title="Physical-AI-Humanoid-Robotics RAG API",
    description="Retrieval-Augmented Generation API for textbook content",
    version="1.0.0"
)

# Include API routers
app.include_router(chat_router, prefix="/api/v1", tags=["chat"])
app.include_router(health_router, prefix="/api/v1", tags=["health"])

@app.get("/")
def read_root():
    return {"message": "Physical-AI-Humanoid-Robotics RAG API"}