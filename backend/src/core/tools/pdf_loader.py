from langchain_community.document_loaders import PyPDFLoader, PyPDFDirectoryLoader
from langchain_core.tools import tool
from langchain.docstore.document import Document

@tool
def load_pdf(path: str) -> Document:
    """
    Load a single PDF file and return its first Document.

    Args:
        path (str): The file path to the PDF.

    Returns:
        Document: The first Document loaded from the PDF file.

    Raises:
        ValueError: If no document is loaded from the PDF.
    """
    loader = PyPDFLoader(path)
    docs = loader.load()
    if not docs:
        raise ValueError(f"No documents were loaded from {path}.")
    return docs[0]

@tool
def load_dir_of_pdfs(path: str) -> list[Document]:
    """
    Load all PDF files in a given directory and return a list of Document objects.

    Args:
        path (str): The directory path containing PDF files.

    Returns:
        List[Document]: A list of Document objects loaded from all PDF files in the directory.

    Raises:
        ValueError: If the provided path is not a directory or no PDFs are loaded.
    """
    
    loader = PyPDFDirectoryLoader(path)
    docs = loader.load()
    if not docs:
        raise ValueError(f"No PDF documents were loaded from directory: {path}.")
    return docs
    