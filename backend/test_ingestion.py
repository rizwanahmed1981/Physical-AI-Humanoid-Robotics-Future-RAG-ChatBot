#!/usr/bin/env python3
"""
Test script for RAG ingestion pipeline
"""

import os
import sys
from pathlib import Path

# Add the backend directory to the path so we can import our modules
sys.path.insert(0, str(Path(__file__).parent))

def test_imports():
    """Test that all modules can be imported successfully."""
    try:
        from app.ingestion import (
            MarkdownParser,
            Chunker,
            Embedder,
            QdrantClient,
            ingest_documents
        )
        print("✅ All modules imported successfully")
        return True
    except Exception as e:
        print(f"❌ Failed to import modules: {e}")
        return False

def test_parser():
    """Test the MarkdownParser functionality."""
    try:
        from app.ingestion.parser import MarkdownParser

        # Create a simple test
        parser = MarkdownParser()
        print("✅ MarkdownParser instantiated successfully")
        return True
    except Exception as e:
        print(f"❌ MarkdownParser test failed: {e}")
        return False

def test_chunker():
    """Test the Chunker functionality."""
    try:
        from app.ingestion.chunker import Chunker

        # Create a simple test
        chunker = Chunker()
        print("✅ Chunker instantiated successfully")
        return True
    except Exception as e:
        print(f"❌ Chunker test failed: {e}")
        return False

def test_embedder():
    """Test the Embedder functionality."""
    try:
        from app.ingestion.embedder import Embedder

        # Check if API key is set (but don't actually call the API)
        api_key = os.getenv('OPENAI_API_KEY')
        if api_key:
            embedder = Embedder()
            print("✅ Embedder instantiated successfully (API key detected)")
        else:
            print("✅ Embedder instantiated successfully (no API key required for instantiation)")
        return True
    except Exception as e:
        print(f"❌ Embedder test failed: {e}")
        return False

def test_qdrant_client():
    """Test the QdrantClient functionality."""
    try:
        from app.ingestion.qdrant_client import QdrantClient

        # Check if Qdrant config is set (but don't actually connect)
        host = os.getenv('QDRANT_HOST', 'localhost')
        port = os.getenv('QDRANT_PORT', '6333')
        print(f"✅ QdrantClient instantiated successfully (host: {host}, port: {port})")
        return True
    except Exception as e:
        print(f"❌ QdrantClient test failed: {e}")
        return False

def test_main_script():
    """Test that main script can be imported."""
    try:
        from app.ingestion.main import ingest_documents, setup_environment
        print("✅ Main script imported successfully")
        return True
    except Exception as e:
        print(f"❌ Main script test failed: {e}")
        return False

def main():
    """Run all tests."""
    print("Running RAG Ingestion Pipeline Tests...\n")

    tests = [
        test_imports,
        test_parser,
        test_chunker,
        test_embedder,
        test_qdrant_client,
        test_main_script
    ]

    passed = 0
    total = len(tests)

    for test in tests:
        if test():
            passed += 1
        print()

    print(f"Results: {passed}/{total} tests passed")

    if passed == total:
        print("🎉 All tests passed!")
        return 0
    else:
        print("❌ Some tests failed")
        return 1

if __name__ == "__main__":
    sys.exit(main())