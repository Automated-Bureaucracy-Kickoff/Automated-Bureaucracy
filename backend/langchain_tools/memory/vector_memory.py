"""
Vector Memory Module

This module implements a memory system that uses vector embeddings to store
and retrieve data based on semantic similarity. Ideal for tasks requiring contextual
search and information retrieval.
"""

from typing import List, Tuple, Dict, Any
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
import os


class VectorMemory:
    """
    A vector-based memory system for semantic search and contextual retrieval.
    """

    def __init__(self, index_path: str = "data/vector_memory_index"):
        """
        Initializes the VectorMemory system.

        Args:
            index_path (str): Path to save the FAISS index file.
        """
        self.index_path = index_path
        self.embedding_model = OpenAIEmbeddings()
        self.vector_store = self._load_or_initialize_index()

    def _load_or_initialize_index(self) -> FAISS:
        """
        Loads an existing FAISS index or initializes a new one.

        Returns:
            FAISS: A vector store instance.
        """
        if os.path.exists(self.index_path):
            return FAISS.load_local(self.index_path, self.embedding_model)
        else:
            return FAISS(self.embedding_model.embed_query, [])

    def add_memory(self, text: str, metadata: Dict[str, Any] = None):
        """
        Adds a memory entry to the vector store.

        Args:
            text (str): The text to add to the memory.
            metadata (dict): Additional metadata to store with the text.
        """
        self.vector_store.add_texts([text], metadatas=[metadata])
        self._save_index()

    def search_memory(self, query: str, top_k: int = 5) -> List[Tuple[str, float, Dict[str, Any]]]:
        """
        Searches the vector store for the most similar entries to the query.

        Args:
            query (str): The query text for semantic search.
            top_k (int): Number of top results to return.

        Returns:
            list: A list of tuples containing the retrieved text, similarity score, and metadata.
        """
        results = self.vector_store.similarity_search_with_score(query, k=top_k)
        return [(res.page_content, score, res.metadata) for res, score in results]

    def delete_memory(self, text: str):
        """
        Deletes a specific memory from the vector store.

        Args:
            text (str): The text to remove from memory.
        """
        self.vector_store.delete_by_text(text)
        self._save_index()

    def _save_index(self):
        """
        Saves the current state of the FAISS index to disk.
        """
        self.vector_store.save_local(self.index_path)

    def list_all_memories(self) -> List[Dict[str, Any]]:
        """
        Lists all stored memories in the vector store.

        Returns:
            list: A list of stored texts and their associated metadata.
        """
        return [{"text": doc.page_content, "metadata": doc.metadata} for doc in self.vector_store.documents]

    def clear_memory(self):
        """
        Clears all stored memories from the vector store.
        """
        self.vector_store = FAISS(self.embedding_model.embed_query, [])
        self._save_index()


if __name__ == "__main__":
    # Example usage
    vm = VectorMemory()

    # Add memories
    vm.add_memory("AI is transforming the world.", {"source": "Research Paper"})
    vm.add_memory("Renewable energy is the future.", {"source": "Whitepaper"})

    # Search for memories
    results = vm.search_memory("What is the future of technology?", top_k=2)
    for text, score, metadata in results:
        print(f"Text: {text}\nScore: {score}\nMetadata: {metadata}\n")

    # List all memories
    print("All Memories:", vm.list_all_memories())

    # Clear memory
    vm.clear_memory()
    print("Memory Cleared:", vm.list_all_memories())
