"""
Chunker for RAG Ingestion Pipeline
Handles splitting content into semantically meaningful chunks.
"""

import re
from typing import List, Dict, Tuple
from collections import OrderedDict
import logging

logger = logging.getLogger(__name__)

class Chunker:
    """Split content into semantically meaningful chunks."""

    def __init__(self, max_chunk_size: int = 500, min_chunk_size: int = 100, overlap: int = 50):
        """
        Initialize chunker with configuration.

        Args:
            max_chunk_size: Maximum number of tokens per chunk
            min_chunk_size: Minimum number of tokens per chunk
            overlap: Number of tokens to overlap between chunks
        """
        self.max_chunk_size = max_chunk_size
        self.min_chunk_size = min_chunk_size
        self.overlap = overlap

    def chunk_sections(self, sections: List[Dict[str, str]]) -> List[Dict[str, str]]:
        """
        Chunk sections into smaller, manageable pieces.

        Args:
            sections: List of section dictionaries

        Returns:
            List of chunk dictionaries
        """
        chunks = []

        for section in sections:
            section_chunks = self._chunk_section(section)
            chunks.extend(section_chunks)

        return chunks

    def _chunk_section(self, section: Dict[str, str]) -> List[Dict[str, str]]:
        """
        Chunk a single section.

        Args:
            section: Section dictionary with title and content

        Returns:
            List of chunk dictionaries
        """
        content = section['content']
        title = section['title']

        # Split content into paragraphs
        paragraphs = self._split_into_paragraphs(content)

        # Create chunks from paragraphs
        chunks = []
        current_chunk = ""
        current_chunk_start = 0

        for i, paragraph in enumerate(paragraphs):
            # Estimate token count (very rough approximation)
            paragraph_tokens = len(paragraph.split())

            # If adding this paragraph would exceed max size, finalize current chunk
            if (len(current_chunk.split()) + paragraph_tokens > self.max_chunk_size and
                len(current_chunk) > self.min_chunk_size):

                # Add current chunk
                chunk_dict = self._create_chunk_dict(
                    current_chunk.strip(),
                    title,
                    section['file_path'],
                    current_chunk_start,
                    i - 1
                )
                chunks.append(chunk_dict)

                # Start new chunk with overlap from previous chunk
                current_chunk = self._get_overlap_content(chunks[-1]['content']) + " " + paragraph
                current_chunk_start = i - 1

            else:
                # Add paragraph to current chunk
                if current_chunk:
                    current_chunk += " " + paragraph
                else:
                    current_chunk = paragraph

        # Add the final chunk
        if current_chunk.strip():
            chunk_dict = self._create_chunk_dict(
                current_chunk.strip(),
                title,
                section['file_path'],
                current_chunk_start,
                len(paragraphs) - 1
            )
            chunks.append(chunk_dict)

        return chunks

    def _split_into_paragraphs(self, content: str) -> List[str]:
        """
        Split content into paragraphs.

        Args:
            content: Content string

        Returns:
            List of paragraphs
        """
        # Split on double newlines (paragraph breaks)
        paragraphs = [p.strip() for p in content.split('\n\n') if p.strip()]
        return paragraphs

    def _get_overlap_content(self, content: str) -> str:
        """
        Get overlapping content from the end of a chunk.

        Args:
            content: Content string

        Returns:
            Overlapping portion of content
        """
        words = content.split()
        if len(words) <= self.overlap:
            return content

        # Take the last overlap words
        return ' '.join(words[-self.overlap:])

    def _create_chunk_dict(self, content: str, section_title: str, file_path: str,
                          start_pos: int, end_pos: int) -> Dict[str, str]:
        """
        Create a chunk dictionary with metadata.

        Args:
            content: Chunk content
            section_title: Title of the section this chunk belongs to
            file_path: Path to the source file
            start_pos: Starting position in the document
            end_pos: Ending position in the document

        Returns:
            Dictionary with chunk metadata
        """
        return {
            'content': content,
            'section_title': section_title,
            'source_file': file_path,
            'chunk_position': (start_pos, end_pos),
            'chunk_type': 'paragraph',  # Could be 'section', 'paragraph', 'code', 'table'
            'chunk_id': self._generate_chunk_id(content, file_path, start_pos),
            'document_id': self._generate_document_id(file_path),
        }

    def _generate_chunk_id(self, content: str, file_path: str, position: int) -> str:
        """
        Generate a unique chunk ID.

        Args:
            content: Chunk content
            file_path: Source file path
            position: Position in document

        Returns:
            Unique chunk ID
        """
        import hashlib
        # Create hash based on content, file, and position
        content_hash = hashlib.md5((content + file_path + str(position)).encode()).hexdigest()
        return f"chunk_{content_hash[:8]}"

    def _generate_document_id(self, file_path: str) -> str:
        """
        Generate a unique document ID.

        Args:
            file_path: Path to the source file

        Returns:
            Unique document ID
        """
        import hashlib
        # Create hash based on file path
        file_hash = hashlib.md5(file_path.encode()).hexdigest()
        return f"doc_{file_hash[:8]}"