"""
Document Context Memory

This module implements a memory system for managing and accessing contextual information
from documents. The memory system allows agents to store and retrieve document-specific
context for enhanced interactions.
"""

from langchain.schema import BaseMemory
from langchain.prompts import PromptTemplate
from typing import Dict, List, Any
import hashlib


class DocumentContextMemory(BaseMemory):
    """
    A memory system designed to manage contextual data extracted from documents.
    """

    def __init__(self):
        """
        Initializes the DocumentContextMemory instance.
        """
        super().__init__()
        self.memory_store: Dict[str, Dict[str, Any]] = {}

    def add_document_context(self, document_id: str, context: str, metadata: Dict[str, Any] = None):
        """
        Adds a document context to the memory store.

        Args:
            document_id (str): Unique identifier for the document.
            context (str): Contextual information extracted from the document.
            metadata (dict): Additional metadata related to the document (optional).
        """
        key = self._generate_hash_key(document_id)
        self.memory_store[key] = {
            "context": context,
            "metadata": metadata or {}
        }

    def retrieve_context(self, document_id: str) -> Dict[str, Any]:
        """
        Retrieves the context of a document using its ID.

        Args:
            document_id (str): Unique identifier for the document.

        Returns:
            dict: A dictionary containing the context and metadata for the document.
        """
        key = self._generate_hash_key(document_id)
        return self.memory_store.get(key, {"context": None, "metadata": None})

    def delete_context(self, document_id: str):
        """
        Deletes a document's context from the memory store.

        Args:
            document_id (str): Unique identifier for the document.
        """
        key = self._generate_hash_key(document_id)
        if key in self.memory_store:
            del self.memory_store[key]

    def list_all_documents(self) -> List[str]:
        """
        Lists all stored document IDs.

        Returns:
            list: A list of document IDs stored in the memory.
        """
        return [self._decode_hash_key(key) for key in self.memory_store.keys()]

    def _generate_hash_key(self, document_id: str) -> str:
        """
        Generates a hashed key for a document ID.

        Args:
            document_id (str): Document ID.

        Returns:
            str: Hashed key.
        """
        return hashlib.sha256(document_id.encode()).hexdigest()

    def _decode_hash_key(self, hashed_key: str) -> str:
        """
        Decodes a hashed key back into a readable document ID (if possible).

        Args:
            hashed_key (str): The hashed key to decode.

        Returns:
            str: Decoded document ID. (Not implemented for security reasons.)
        """
        # Implement decoding if needed; for now, return the hashed key as a placeholder.
        return hashed_key

    def as_prompt_template(self) -> PromptTemplate:
        """
        Converts the memory into a prompt template for LangChain.

        Returns:
            PromptTemplate: A prompt template encapsulating the stored contexts.
        """
        context_summary = "\n".join(
            [f"Document ID: {doc_id}\nContext: {entry['context']}" for doc_id, entry in self.memory_store.items()]
        )
        return PromptTemplate(
            input_variables=["query"],
            template=f"""
                You have access to the following document contexts:
                {context_summary}

                Based on this information, answer the following query:
                {{query}}
            """
        )


if __name__ == "__main__":
    # Example usage
    memory = DocumentContextMemory()

    # Add documents
    memory.add_document_context("doc1", "AI is transforming the world.", {"source": "Research Paper"})
    memory.add_document_context("doc2", "Renewable energy is the future.", {"source": "Whitepaper"})

    # Retrieve document context
    context = memory.retrieve_context("doc1")
    print("Retrieved Context:", context)

    # List all documents
    all_docs = memory.list_all_documents()
    print("All Documents:", all_docs)

    # Delete a document
    memory.delete_context("doc1")
    print("After Deletion:", memory.list_all_documents())

    # Convert to prompt template
    prompt = memory.as_prompt_template()
    print("Generated Prompt Template:", prompt.template)
