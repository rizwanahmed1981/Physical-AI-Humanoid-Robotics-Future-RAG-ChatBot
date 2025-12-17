# Implementation Plan: RAG Ingestion Pipeline

**Branch**: `002-rag-system` | **Date**: 2025-12-17 | **Spec**: specs/002-rag-system/spec.md
**Input**: Feature specification from `/specs/002-rag-system/spec.md`

## Summary

This implementation plan outlines the approach for designing a step-by-step ingestion pipeline to process textbook content into a vector database for use by a Retrieval-Augmented Generation (RAG) system. The pipeline will handle parsing markdown files, chunking content, generating embeddings, and storing data in Qdrant Cloud.

## Technical Context

**Language/Version**: Python 3.10+
**Primary Dependencies**:
- markdown (for parsing)
- openai (for embeddings)
- qdrant-client (for Qdrant Cloud)
- fastapi (existing backend structure)
**Storage**: Qdrant Cloud (free tier)
**Testing**: Unit tests for parsing and chunking logic
**Target Platform**: Backend service
**Project Type**: Data processing pipeline
**Performance Goals**: Efficient ingestion with minimal memory overhead
**Constraints**:
- Must process markdown files from frontend/docs/
- Must exclude quizzes, UI components, and answer keys
- Must maintain metadata for citations
- Must support local execution flow
- Must verify data storage in Qdrant

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

The implementation plan adheres to the constitution principles:
- **Source Fidelity and Truthfulness**: Content is parsed from official textbook markdown files
- **Core Educational Mission**: Content is preserved for educational purposes
- **Audience Awareness**: Designed for AI learners with no robotics experience
- **Clarity Over Cleverness**: Clear, straightforward processing pipeline
- **AI-Native Writing Principles**: Content structured for retrieval and generation
- **Emotional and Motivational Resonance**: Enables learning through interactive Q&A
- **Structured Assessment as a Core Feature**: Supports quiz creation through content processing
- **Quiz Design Standards**: Content is processed to exclude quiz materials
- **Interactive Answer Reveal Requirement**: Content prepared for interactive responses
- **Pedagogical Flow Control**: Content organized for logical progression

## Project Structure

### Documentation (this feature)

```text
specs/002-rag-system/
├── plan.md              # This file (/sp.plan command output)
├── research.md          # Phase 0 output (/sp.plan command)
├── data-model.md        # Phase 1 output (/sp.plan command)
├── quickstart.md        # Phase 1 output (/sp.plan command)
├── contracts/           # Phase 1 output (/sp.plan command)
└── tasks.md             # Phase 2 output (/sp.tasks command - NOT created by /sp.plan)
```

### Source Code (repository root)

```text
# [REMOVE IF UNUSED] Option 1: Single project (DEFAULT)
backend/
├── app/
│   ├── ingestion/
│   │   ├── __init__.py
│   │   ├── parser.py
│   │   ├── chunker.py
│   │   ├── embedder.py
│   │   ├── qdrant_client.py
│   │   └── main.py
│   └── utils/
│       └── validators.py
└── requirements.txt
```

**Structure Decision**: This is a data processing pipeline, so we'll place ingestion components in backend/app/ingestion/ directory.

## Complexity Tracking

> **Fill ONLY if Constitution Check has violations that must be justified**

| Violation | Why Needed | Simpler Alternative Rejected Because |
|-----------|------------|-------------------------------------|

## Phase 0: Research & Outline

This phase will focus on defining the content structure and research any specific aspects that need clarification.

## Phase 1: Design & Implementation

This phase will produce the actual implementation design for the ingestion pipeline including:
1. Markdown parsing strategy
2. Content filtering rules
3. Chunking strategy
4. Metadata schema
5. Qdrant integration approach

## Phase 2: Implementation Tasks

Tasks will be generated in a separate tasks.md file using `/sp.tasks` command.

## File and Module Responsibilities

### Chunking Module (`chunker.py`)
- Split markdown content into semantically meaningful chunks
- Maintain context between chunks
- Handle section boundaries appropriately
- Support configurable chunk sizes

### Ingestion Module (`main.py`)
- Orchestrates the ingestion process
- Coordinates parsing, chunking, embedding, and storage
- Handles error cases and retries
- Manages execution flow

### Embedding Module (`embedder.py`)
- Generates vector embeddings using OpenAI API
- Handles batching for efficiency
- Manages rate limiting
- Stores embeddings in memory or temporary cache

### Qdrant Client Module (`qdrant_client.py`)
- Connects to Qdrant Cloud instance
- Handles data insertion and retrieval
- Manages collections and vectors
- Implements error handling for network issues

## Markdown Parsing Strategy

- Parse markdown files using markdown library
- Extract text content while preserving structure
- Identify headers to maintain semantic boundaries
- Extract code blocks separately for specialized handling
- Preserve emphasis and formatting where relevant
- Handle table content appropriately

## Content Filtering Rules

### Excluded Content:
- Quiz questions and answers (identified by specific patterns)
- UI components and templates
- Answer keys and solutions
- Navigation elements
- Images and media references
- Appendix sections (if not needed for core content)

### Included Content:
- Main text content
- Code examples with explanations
- Figures and diagrams (as text descriptions)
- Tables with data
- Section headers and titles
- Bullet points and lists

## Chunking Strategy

### Approach:
- Split content by section boundaries (headers)
- Use sliding window technique for overlapping context
- Maximum chunk size: 500 tokens
- Minimum chunk size: 100 tokens
- Overlap between chunks: 50 tokens
- Preserve semantic meaning in each chunk

### Chunk Types:
1. **Section chunks**: Full sections with headers
2. **Paragraph chunks**: Individual paragraphs
3. **Code chunks**: Code blocks with context
4. **Table chunks**: Table data with surrounding text

## Metadata Schema

### Required Fields:
- **document_id**: Unique identifier for source document
- **chunk_id**: Unique identifier for chunk within document
- **source_file**: Path to original markdown file
- **section_title**: Title of section containing chunk
- **chunk_position**: Position within document (start, end)
- **chunk_type**: Type of content (section, paragraph, code, etc.)
- **created_at**: Timestamp of ingestion
- **embedding_version**: Version of embedding model used

### Optional Fields:
- **chapter_number**: Chapter identifier
- **section_number**: Section identifier
- **tags**: Content categories
- **related_chunks**: IDs of related chunks for context

## Environment Variable Usage

### Required Variables:
- `OPENAI_API_KEY`: API key for OpenAI embeddings
- `QDRANT_HOST`: Host address for Qdrant Cloud instance
- `QDRANT_PORT`: Port for Qdrant connection
- `QDRANT_API_KEY`: API key for Qdrant Cloud (if required)
- `INPUT_DIR`: Directory containing markdown files
- `OUTPUT_DIR`: Directory for temporary processing files

### Default Values:
- `INPUT_DIR`: frontend/docs/
- `OUTPUT_DIR`: temp/ingestion/

## Error Handling and Validation Steps

1. **File Validation**:
   - Verify markdown files exist
   - Check file permissions
   - Validate file encoding

2. **Content Validation**:
   - Check for empty documents
   - Validate section structure
   - Ensure minimum content length

3. **Processing Validation**:
   - Validate chunk sizes
   - Verify embedding generation
   - Check Qdrant connectivity

4. **Error Recovery**:
   - Retry failed embeddings with exponential backoff
   - Log failed files for manual review
   - Continue processing other files on individual failures

## Local Execution Flow

1. Set environment variables
2. Run ingestion script: `python backend/app/ingestion/main.py`
3. Script processes all markdown files in INPUT_DIR
4. Generates chunks and embeddings
5. Stores data in Qdrant Cloud
6. Reports completion status and statistics

## Verification Steps

1. **Pre-Verification**:
   - Validate input directory structure
   - Check Qdrant connection
   - Verify API keys

2. **During Processing**:
   - Monitor progress indicators
   - Log processing statistics
   - Track errors and warnings

3. **Post-Processing**:
   - Verify document count in Qdrant
   - Validate chunk count per document
   - Check embedding generation success rate
   - Confirm metadata integrity

4. **Final Validation**:
   - Run sample retrieval queries
   - Verify citation accuracy
   - Test error handling scenarios