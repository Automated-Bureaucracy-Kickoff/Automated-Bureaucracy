"""
Document Parser Tool
This module defines the DocumentParserTool class, which processes and extracts meaningful information from documents.
"""

from typing import Dict, Any, List
from langchain.document_loaders import PyPDFLoader, DocxLoader, TextLoader
from langchain.text_splitter import CharacterTextSplitter


class DocumentParserTool:
    """
    Tool to parse and extract information from various document formats.
    """

    def __init__(self):
        """
        Initialize the document parser tool.
        """
        self.supported_formats = ["pdf", "docx", "txt"]

    def parse_document(self, file_path: str, file_type: str = None) -> Dict[str, Any]:
        """
        Parse a document and extract its content.

        Args:
            file_path (str): The path to the document file.
            file_type (str, optional): The type of the file (e.g., 'pdf', 'docx', 'txt'). 
                                       If not provided, it will be inferred from the file extension.

        Returns:
            Dict[str, Any]: Parsed content, including metadata and text.
        """
        if file_type is None:
            file_type = self._infer_file_type(file_path)

        if file_type not in self.supported_formats:
            raise ValueError(f"Unsupported file type: {file_type}. Supported formats: {self.supported_formats}")

        loader = self._get_loader(file_path, file_type)
        if loader is None:
            raise ValueError(f"No loader available for file type: {file_type}")

        documents = loader.load()
        text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
        split_texts = text_splitter.split_documents(documents)

        return {
            "file_path": file_path,
            "file_type": file_type,
            "content": split_texts,
            "metadata": self._extract_metadata(file_path),
        }

    def _get_loader(self, file_path: str, file_type: str):
        """
        Get the appropriate loader for the file type.

        Args:
            file_path (str): The path to the file.
            file_type (str): The file type.

        Returns:
            Loader instance or None if no loader is available.
        """
        if file_type == "pdf":
            return PyPDFLoader(file_path)
        elif file_type == "docx":
            return DocxLoader(file_path)
        elif file_type == "txt":
            return TextLoader(file_path)
        else:
            return None

    def _infer_file_type(self, file_path: str) -> str:
        """
        Infer the file type from the file extension.

        Args:
            file_path (str): The path to the file.

        Returns:
            str: The inferred file type.
        """
        return file_path.split(".")[-1].lower()

    def _extract_metadata(self, file_path: str) -> Dict[str, Any]:
        """
        Extract metadata from the document file.

        Args:
            file_path (str): The path to the document file.

        Returns:
            Dict[str, Any]: Extracted metadata (e.g., file name, size).
        """
        import os

        file_name = os.path.basename(file_path)
        file_size = os.path.getsize(file_path)

        return {
            "file_name": file_name,
            "file_size_bytes": file_size,
        }


# Example Usage
if __name__ == "__main__":
    parser = DocumentParserTool()

    # Parse a sample PDF file
    try:
        result = parser.parse_document("sample.pdf")
        print("Parsed Content:", result["content"])
        print("Metadata:", result["metadata"])
    except Exception as e:
        print(f"Error parsing document: {e}")

    # Parse a sample DOCX file
    try:
        result = parser.parse_document("sample.docx")
        print("Parsed Content:", result["content"])
        print("Metadata:", result["metadata"])
    except Exception as e:
        print(f"Error parsing document: {e}")

    # Parse a sample TXT file
    try:
        result = parser.parse_document("sample.txt")
        print("Parsed Content:", result["content"])
        print("Metadata:", result["metadata"])
    except Exception as e:
        print(f"Error parsing document: {e}")
