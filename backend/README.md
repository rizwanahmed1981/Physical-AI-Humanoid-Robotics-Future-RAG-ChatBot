# Physical-AI-Humanoid-Robotics RAG Backend

This directory contains the backend service for the Physical-AI-Humanoid-Robotics textbook, implementing a Retrieval-Augmented Generation (RAG) system using FastAPI.

## Architecture

The backend implements a modular architecture with the following components:

1. **FastAPI Application** (`app/main.py`) - Main API entry point
2. **API Routes** (`app/api/`) - REST endpoints for chat and health checks
3. **RAG Agents** (`app/agents/`) - AI agents for processing queries and generating responses
4. **Services** (`app/services/`) - Core services for embeddings, retrieval, and generation
5. **Configuration** (`app/config.py`) - Application configuration

## Features

- **RAG-powered Chat**: Retrieve relevant textbook content and generate contextual responses
- **Quiz Generation**: Generate quiz questions based on textbook content
- **Health Checks**: Monitor API status and readiness
- **Docker Support**: Containerized deployment ready

## Getting Started

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run the development server:
```bash
uvicorn app.main:app --reload
```

3. Access the API at `http://localhost:8000`

## API Endpoints

- `GET /health` - Health check
- `GET /ready` - Readiness check
- `POST /api/v1/chat` - Chat endpoint with RAG capabilities
- `POST /api/v1/chat-stream` - Streaming chat endpoint

## Directory Structure

```
backend/
├── app/
│   ├── main.py              # FastAPI entry point
│   ├── api/
│   │   ├── chat.py          # Chat endpoints
│   │   └── health.py        # Health endpoints
│   ├── agents/
│   │   ├── rag_agent.py     # RAG processing agent
│   │   └── quiz_agent.py    # Quiz generation agent
│   ├── services/
│   │   ├── embedding.py     # Embedding generation
│   │   ├── retrieval.py     # Content retrieval
│   │   └── generation.py    # Response generation
│   └── config.py            # Configuration
├── requirements.txt         # Python dependencies
├── Dockerfile               # Container configuration
└── README.md                # This file
```