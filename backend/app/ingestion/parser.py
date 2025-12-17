"""
Markdown Parser for RAG Ingestion Pipeline
Handles parsing of markdown files and filtering of unwanted content.
"""

import os
import re
from typing import List, Dict, Tuple
from pathlib import Path
import logging

logger = logging.getLogger(__name__)

class MarkdownParser:
    """Parse markdown files and extract content while filtering unwanted elements."""

    def __init__(self):
        # Patterns to identify quiz content that should be excluded
        self.quiz_patterns = [
            r'##\s*Quiz\s*.*',
            r'###\s*Quiz\s*.*',
            r'####\s*Quiz\s*.*',
            r'##\s*Answers?\s*.*',
            r'###\s*Answers?\s*.*',
            r'####\s*Answers?\s*.*',
            r'##\s*Exercise\s*.*',
            r'###\s*Exercise\s*.*',
            r'####\s*Exercise\s*.*',
            r'\*\*\s*Answer:\s*\*\*',
            r'\*\*\s*Solution:\s*\*\*',
            r'\*\*\s*Correct\s*Answer:\s*\*\*',
            r'```.*quiz.*',
            r'```.*answer.*',
            r'```.*solution.*',
        ]

        # Patterns to identify UI components and templates
        self.ui_patterns = [
            r'<!--\s*UI\s*.*?-->',
            r'<!--\s*TEMPLATE\s*.*?-->',
            r'<div\s+class=".*ui.*">.*?</div>',
            r'<button.*?>.*?</button>',
            r'<input.*?>',
            r'<select.*?>.*?</select>',
            r'<form.*?>.*?</form>',
            r'\[.*\]\(.*\)\s*-\s*UI\s*Component',
        ]

        # Patterns to identify media references that should be excluded
        self.media_patterns = [
            r'!\[.*\]\(.*\)',
            r'<img.*?>',
            r'<video.*?>.*?</video>',
            r'<audio.*?>.*?</audio>',
        ]

    def parse_file(self, file_path: str) -> Dict[str, str]:
        """
        Parse a markdown file and extract content while filtering unwanted elements.

        Args:
            file_path: Path to the markdown file

        Returns:
            Dictionary with file metadata and filtered content
        """
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()

            # Extract metadata
            metadata = self._extract_metadata(content)

            # Filter content
            filtered_content = self._filter_content(content)

            # Extract sections
            sections = self._extract_sections(filtered_content)

            return {
                'file_path': file_path,
                'filename': os.path.basename(file_path),
                'sections': sections,
                'metadata': metadata,
                'content': filtered_content
            }

        except Exception as e:
            logger.error(f"Error parsing file {file_path}: {str(e)}")
            raise

    def _extract_metadata(self, content: str) -> Dict[str, str]:
        """Extract metadata from markdown content."""
        metadata = {}

        # Look for YAML front matter
        yaml_match = re.search(r'^---\n(.*?)\n---', content, re.DOTALL)
        if yaml_match:
            yaml_content = yaml_match.group(1)
            # Simple YAML parsing for basic metadata
            for line in yaml_content.split('\n'):
                if ':' in line:
                    key, value = line.split(':', 1)
                    metadata[key.strip()] = value.strip()

        return metadata

    def _filter_content(self, content: str) -> str:
        """
        Filter out unwanted content like quizzes, UI components, and media references.

        Args:
            content: Raw markdown content

        Returns:
            Filtered content string
        """
        # Remove quiz content
        filtered_content = content
        for pattern in self.quiz_patterns:
            filtered_content = re.sub(pattern, '', filtered_content, flags=re.IGNORECASE | re.MULTILINE)

        # Remove UI components
        for pattern in self.ui_patterns:
            filtered_content = re.sub(pattern, '', filtered_content, flags=re.IGNORECASE | re.MULTILINE)

        # Remove media references
        for pattern in self.media_patterns:
            filtered_content = re.sub(pattern, '', filtered_content, flags=re.IGNORECASE | re.MULTILINE)

        # Remove empty lines and trim whitespace
        lines = filtered_content.split('\n')
        filtered_lines = [line.strip() for line in lines if line.strip()]
        filtered_content = '\n'.join(filtered_lines)

        return filtered_content

    def _extract_sections(self, content: str) -> List[Dict[str, str]]:
        """
        Extract sections from content based on headers.

        Args:
            content: Filtered content

        Returns:
            List of section dictionaries with title and content
        """
        sections = []
        lines = content.split('\n')

        current_section = None
        section_content = []

        for line in lines:
            # Check if line is a header
            header_match = re.match(r'^(#{1,6})\s+(.*)', line)
            if header_match:
                # Save previous section if exists
                if current_section:
                    sections.append({
                        'title': current_section,
                        'content': '\n'.join(section_content).strip(),
                        'level': len(header_match.group(1))
                    })

                # Start new section
                current_section = header_match.group(2).strip()
                section_content = []
            else:
                # Add content to current section
                if current_section is not None:
                    section_content.append(line)

        # Don't forget the last section
        if current_section:
            sections.append({
                'title': current_section,
                'content': '\n'.join(section_content).strip(),
                'level': 0
            })

        return sections

    def parse_directory(self, directory_path: str) -> List[Dict[str, str]]:
        """
        Parse all markdown files in a directory.

        Args:
            directory_path: Path to directory containing markdown files

        Returns:
            List of parsed document dictionaries
        """
        documents = []
        directory = Path(directory_path)

        if not directory.exists():
            raise FileNotFoundError(f"Directory {directory_path} does not exist")

        # Find all markdown files
        md_files = directory.glob('**/*.md')

        for file_path in md_files:
            try:
                doc = self.parse_file(str(file_path))
                documents.append(doc)
            except Exception as e:
                logger.warning(f"Failed to parse {file_path}: {str(e)}")
                continue

        return documents