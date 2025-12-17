---
description: "Task list for restructuring repository: frontend/backend separation and RAG chatbot scaffolding"
---

# Tasks: Repository Restructure - Frontend/Backend Separation

**Input**: User requirements for separating frontend and backend concerns
**Prerequisites**: None required for restructuring tasks

**Tests**: None (structural changes only)

**Organization**: Tasks are grouped by implementation phase to enable systematic restructuring.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- **Frontend**: `frontend/` directory
- **Backend**: `backend/` directory
- **Specs**: `specs/` directory
- **Claude**: `.claude/` directory (root)

## Phase 1: Setup (Repository Restructuring Foundation)

**Purpose**: Create new directory structure and move files to appropriate locations

- [X] T001 Create frontend directory structure
- [X] T002 Create backend directory structure
- [X] T003 Create backend app directory structure
- [X] T004 Create backend api directory structure
- [X] T005 Create backend agents directory structure
- [X] T006 Create backend services directory structure

---

## Phase 2: Frontend Migration (Docusaurus Content)

**Purpose**: Move all Docusaurus-related files to frontend directory

- [X] T007 [P] Move docs/ to frontend/docs/
- [X] T008 [P] Move src/ to frontend/src/
- [X] T009 [P] Move static/ to frontend/static/
- [X] T010 Move docusaurus.config.js to frontend/docusaurus.config.js
- [X] T011 Move sidebars.js to frontend/sidebars.js
- [X] T012 Move package.json to frontend/package.json
- [X] T013 Move package-lock.json to frontend/package-lock.json

---

## Phase 3: Backend Scaffolding (RAG Chatbot Structure)

**Purpose**: Create backend structure with placeholder files for FastAPI application

- [X] T014 Create backend/app/main.py with FastAPI app structure
- [X] T015 Create backend/app/api/chat.py with RAG endpoints structure
- [X] T016 Create backend/app/api/health.py with health check endpoint
- [X] T017 Create backend/app/agents/rag_agent.py with agent structure
- [X] T018 Create backend/app/agents/quiz_agent.py with quiz agent structure
- [X] T019 Create backend/app/services/embedding.py with embedding service structure
- [X] T020 Create backend/app/services/retrieval.py with retrieval service structure
- [X] T021 Create backend/app/services/generation.py with generation service structure
- [X] T022 Create backend/app/config.py with configuration structure
- [X] T023 Create backend/requirements.txt with FastAPI dependencies
- [X] T024 Create backend/Dockerfile with container configuration
- [X] T025 Create backend/README.md with backend documentation

---

## Phase 4: Frontend Documentation (Frontend README)

**Purpose**: Create documentation for frontend application

- [X] T026 Create frontend/README.md with frontend documentation

---

## Phase 5: Specification Organization (Specs Cleanup)

**Purpose**: Ensure all Spec-Kit Plus files remain under specs/ directory

- [X] T027 Verify specs/ directory contains all specification files
- [X] T028 Move any spec files outside specs/ directory to proper location if needed

---

## Phase 6: Root Directory Cleanup

**Purpose**: Ensure root directory contains only top-level files

- [X] T029 Update root README.md to reflect new structure
- [X] T030 Verify .claude/ directory remains at root
- [X] T031 Remove any old files from root that are now in frontend/

---

## Phase 7: Configuration Updates (Cross-Reference Fixes)

**Purpose**: Update any configuration files to reference new paths

- [X] T032 Update any path references in moved files to reflect new structure
- [X] T033 Verify GitHub Pages deployment configuration still works with new structure

---

## Phase 8: Validation & Testing

**Purpose**: Verify the restructuring was successful

- [X] T034 Verify frontend directory contains all Docusaurus files
- [X] T035 Verify backend directory contains all FastAPI files
- [X] T036 Test frontend build process in frontend/ directory
- [X] T037 Verify all specs remain in specs/ directory
- [X] T038 Confirm .claude/ directory remains at root
- [X] T039 Document the new directory structure for future reference

---

## Dependencies & Execution Order

### Phase Dependencies
- **Setup (Phase 1)**: No dependencies - can start immediately
- **Frontend Migration (Phase 2)**: Depends on Setup completion
- **Backend Scaffolding (Phase 3)**: Depends on Setup completion
- **Frontend Documentation (Phase 4)**: Depends on Frontend Migration completion
- **Specification Organization (Phase 5)**: Can run in parallel with other phases
- **Root Directory Cleanup (Phase 6)**: Depends on migration completion
- **Configuration Updates (Phase 7)**: Depends on all migrations
- **Validation & Testing (Phase 8)**: Depends on all previous phases

### Parallel Opportunities
- All Setup tasks (T001-T006) can run in parallel
- All Frontend Migration tasks marked [P] can run in parallel
- All Backend scaffolding files can be created in parallel after directory structure exists

---

## Implementation Strategy

### Complete Restructuring
1. Complete Phase 1: Setup (directory structure)
2. Complete Phase 2: Frontend Migration (file moves)
3. Complete Phase 3: Backend Scaffolding (file creation)
4. Complete Phase 4: Frontend Documentation
5. Complete Phase 5: Specification Organization
6. Complete Phase 6: Root Directory Cleanup
7. Complete Phase 7: Configuration Updates
8. Complete Phase 8: Validation & Testing

### Verification Steps
- Ensure frontend remains deployable to GitHub Pages
- Verify backend has complete FastAPI structure
- Confirm all specs remain accessible under specs/
- Verify .claude/ directory remains at root level