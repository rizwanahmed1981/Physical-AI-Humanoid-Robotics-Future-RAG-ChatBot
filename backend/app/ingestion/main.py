"""
Main ingestion script for RAG pipeline
 orchestrates the entire ingestion process.
"""

import os
import sys
import logging
from typing import List, Dict, Any
import argparse
from pathlib import Path

# Add backend to path so we can import our modules
sys.path.insert(0, str(Path(__file__).parent.parent))

from ingestion.parser import MarkdownParser
from ingestion.chunker import Chunker
from ingestion.embedder import Embedder
from ingestion.qdrant_client import QdrantClient

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def setup_environment():
    """Setup environment variables and validate configuration."""
    # Check required environment variables
    required_vars = ['OPENAI_API_KEY']

    for var in required_vars:
        if not os.getenv(var):
            raise ValueError(f"Required environment variable {var} is not set")

    # Set defaults for optional variables
    if not os.getenv('QDRANT_HOST'):
        os.environ['QDRANT_HOST'] = 'localhost'

    if not os.getenv('QDRANT_PORT'):
        os.environ['QDRANT_PORT'] = '6333'

    if not os.getenv('INPUT_DIR'):
        os.environ['INPUT_DIR'] = 'frontend/docs/'

    if not os.getenv('OUTPUT_DIR'):
        os.environ['OUTPUT_DIR'] = 'temp/ingestion/'

def ingest_documents(input_dir: str = None, output_dir: str = None,
                     collection_name: str = "textbook_content") -> Dict[str, Any]:
    """
    Main ingestion function to process markdown files and store in Qdrant.

    Args:
        input_dir: Directory containing markdown files
        output_dir: Directory for temporary processing files
        collection_name: Name of Qdrant collection to use

    Returns:
        Dictionary with ingestion statistics
    """
    # Setup environment
    setup_environment()

    # Get input/output directories from environment or parameters
    input_dir = input_dir or os.getenv('INPUT_DIR', 'frontend/docs/')
    output_dir = output_dir or os.getenv('OUTPUT_DIR', 'temp/ingestion/')

    logger.info(f"Starting ingestion process")
    logger.info(f"Input directory: {input_dir}")
    logger.info(f"Output directory: {output_dir}")
    logger.info(f"Collection name: {collection_name}")

    try:
        # Create output directory if it doesn't exist
        Path(output_dir).mkdir(parents=True, exist_ok=True)

        # Initialize components
        parser = MarkdownParser()
        chunker = Chunker()
        embedder = Embedder()
        qdrant_client = QdrantClient()

        # Parse all markdown files
        logger.info("Parsing markdown files...")
        documents = parser.parse_directory(input_dir)
        logger.info(f"Parsed {len(documents)} documents")

        # Chunk content
        logger.info("Chunking content...")
        all_chunks = []
        for doc in documents:
            sections = doc['sections']
            chunks = chunker.chunk_sections(sections)
            all_chunks.extend(chunks)

        logger.info(f"Created {len(all_chunks)} chunks")

        # Generate embeddings
        logger.info("Generating embeddings...")
        chunks_with_embeddings = embedder.generate_embeddings_for_chunks(all_chunks)
        logger.info("Embeddings generated successfully")

        # Store in Qdrant
        logger.info("Storing in Qdrant...")
        points_upserted = qdrant_client.upsert_chunks(collection_name, chunks_with_embeddings)
        logger.info(f"Successfully upserted {points_upserted} points")

        # Get collection info for verification
        collection_info = qdrant_client.get_collection_info(collection_name)
        logger.info(f"Collection info: {collection_info}")

        # Return statistics
        stats = {
            'documents_processed': len(documents),
            'chunks_created': len(all_chunks),
            'points_upserted': points_upserted,
            'collection_name': collection_name,
            'collection_info': collection_info
        }

        logger.info("Ingestion process completed successfully")
        return stats

    except Exception as e:
        logger.error(f"Ingestion failed: {str(e)}")
        raise

def main():
    """Main entry point for the ingestion script."""
    parser = argparse.ArgumentParser(description='RAG Ingestion Pipeline')
    parser.add_argument('--input-dir', help='Input directory containing markdown files')
    parser.add_argument('--output-dir', help='Output directory for temporary files')
    parser.add_argument('--collection-name', default='textbook_content',
                       help='Name of Qdrant collection')

    args = parser.parse_args()

    try:
        stats = ingest_documents(
            input_dir=args.input_dir,
            output_dir=args.output_dir,
            collection_name=args.collection_name
        )

        print("Ingestion completed successfully!")
        print(f"Documents processed: {stats['documents_processed']}")
        print(f"Chunks created: {stats['chunks_created']}")
        print(f"Points upserted: {stats['points_upserted']}")
        print(f"Collection: {stats['collection_name']}")

    except Exception as e:
        logger.error(f"Failed to run ingestion: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()