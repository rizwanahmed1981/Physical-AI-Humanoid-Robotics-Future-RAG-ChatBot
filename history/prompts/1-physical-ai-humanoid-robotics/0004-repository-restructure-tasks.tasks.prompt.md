---
id: "0004"
title: "Repository Restructure Tasks"
stage: "tasks"
date_iso: "2025-12-17"
surface: "agent"
model: "claude-sonnet-4-5-20250929"
feature: "1-physical-ai-humanoid-robotics"
branch: "main"
user: "ecomw"
command: "/sp.tasks"
labels: ["restructure", "frontend", "backend", "rag"]
spec: null
ticket: null
adr: null
pr: null
files:
  - "specs/1-physical-ai-humanoid-robotics/restructure-tasks.md"
tests: []
---

# Repository Restructure Tasks

## Summary
Generated tasks for restructuring the repository to separate frontend and backend concerns, with scaffolding for a future RAG chatbot. The tasks focus on moving Docusaurus files to a frontend directory and creating a FastAPI backend structure.

## Changes Made
- Created restructure-tasks.md with 39 tasks organized in 8 phases
- Tasks cover frontend migration, backend scaffolding, and validation
- All tasks follow the required checklist format with proper IDs and labels

## Task Distribution
- Setup: 6 tasks
- Frontend Migration: 7 tasks
- Backend Scaffolding: 12 tasks
- Documentation: 1 task
- Organization: 2 tasks
- Cleanup: 3 tasks
- Configuration: 2 tasks
- Validation: 6 tasks

## Key Outcomes
- Frontend files will be moved to frontend/ directory
- Backend structure with FastAPI app will be created in backend/
- All specs remain in specs/ directory
- .claude/ directory stays at root level
- Repository maintains deployability to GitHub Pages

## Prompt Text
```
You are working on the project:

Physical-AI-Humanoid-Robotics-Future

Your task is to RESTRUCTURE the repository to clearly separate frontend and backend concerns, and scaffold the backend for a future RAG chatbot.

### High-Level Goal
- Frontend: Docusaurus-based AI-native textbook
- Backend: FastAPI-based RAG system using OpenAI Agents SDK

### Critical Rules
- Do NOT modify book content
- Do NOT regenerate chapters
- Do NOT change documentation text
- Do NOT invent new features
- Only move files and scaffold structure

### Step 1: Frontend Separation
Move all Docusaurus-related files into a new `frontend/` directory, including:
- docs/
- src/
- static/
- docusaurus.config.js
- sidebars.js
- package.json
- package-lock.json

Ensure the frontend remains deployable to GitHub Pages.

### Step 2: Backend Creation
Create a new `backend/` directory and scaffold a FastAPI application with:
- app/main.py
- app/api/chat.py
- app/agents/rag_agent.py
- app/services/embedding.py
- app/services/retrieval.py
- app/services/generation.py
- requirements.txt

The backend is for:
- Retrieval-Augmented Generation over book content
- Agent-based reasoning
- Future personalization

No implementation logic yet, only structure and placeholders.

### Step 3: Specs Organization
Ensure all Spec-Kit Plus files live under:
- specs/

Do not change their content.

### Step 4: Claude Governance
Ensure `.claude/` remains at the root and is not duplicated.

### Output Rules
- Show the final directory tree
- Show file move operations clearly
- Do NOT include code implementations
- Do NOT explain reasoning
 Physical-AI-Humanoid-Robotics-Future/
│
├── frontend/
│   ├── docs/
│   ├── src/
│   ├── static/
│   ├── docusaurus.config.js
│   ├── sidebars.js
│   ├── package.json
│   └── README.md
│
├── backend/
│   ├── app/
│   │   ├── main.py              # FastAPI entry
│   │   ├── api/
│   │   │   ├── chat.py           # RAG endpoints
│   │   │   └── health.py
│   │   ├── agents/
│   │   │   ├── rag_agent.py
│   │   │   └── quiz_agent.py
│   │   ├── services/
│   │   │   ├── embedding.py
│   │   │   ├── retrieval.py
│   │   │   └── generation.py
│   │   └── config.py
│   │
│   ├── requirements.txt
│   ├── Dockerfile
│   └── README.md
│
├── specs/
│   ├── sp.constitution.md
│   ├── sp.task.md
│   ├── sp.implementation.md
│   └── rag.spec.md
│
├── .claude/
│   └── instructions.md
│
├── README.md
```

## Response Text
Created restructure-tasks.md with 39 structured tasks across 8 phases to restructure the repository with separate frontend/backend directories while preserving all existing content.

## Outcome
Successfully generated comprehensive task list for repository restructuring with clear phases and dependencies.

## Evaluation
The generated tasks follow the required format and address all requirements: frontend separation, backend scaffolding, spec organization, and Claude governance.