"""
Long-Term Memory Module

This module provides a system for managing long-term memory for agents. It stores
and retrieves historical data for improved decision-making and contextual understanding.
"""

from typing import Dict, Any, List
from langchain.schema import BaseMemory
import os
import json


class LongTermMemory(BaseMemory):
    """
    A long-term memory system for storing and retrieving persistent knowledge across sessions.
    """

    def __init__(self, storage_path: str = "data/long_term_memory.json"):
        """
        Initializes the long-term memory system.

        Args:
            storage_path (str): Path to the JSON file for persistent storage.
        """
        super().__init__()
        self.storage_path = storage_path
        self.memory_store: Dict[str, Any] = self._load_memory()

    def _load_memory(self) -> Dict[str, Any]:
        """
        Loads memory data from the storage file.

        Returns:
            dict: The memory data loaded from the file.
        """
        if os.path.exists(self.storage_path):
            with open(self.storage_path, "r") as file:
                return json.load(file)
        return {}

    def _save_memory(self):
        """
        Saves the current memory data to the storage file.
        """
        with open(self.storage_path, "w") as file:
            json.dump(self.memory_store, file, indent=4)

    def add_memory(self, key: str, value: Any):
        """
        Adds an entry to long-term memory.

        Args:
            key (str): The key for the memory entry.
            value (Any): The value to associate with the key.
        """
        self.memory_store[key] = value
        self._save_memory()

    def get_memory(self, key: str) -> Any:
        """
        Retrieves a memory entry by key.

        Args:
            key (str): The key for the memory entry.

        Returns:
            Any: The value associated with the key, or None if the key does not exist.
        """
        return self.memory_store.get(key)

    def delete_memory(self, key: str):
        """
        Deletes a memory entry by key.

        Args:
            key (str): The key for the memory entry.
        """
        if key in self.memory_store:
            del self.memory_store[key]
            self._save_memory()

    def list_memory_keys(self) -> List[str]:
        """
        Lists all keys in the long-term memory.

        Returns:
            list: A list of all memory keys.
        """
        return list(self.memory_store.keys())

    def clear_memory(self):
        """
        Clears all long-term memory.
        """
        self.memory_store.clear()
        self._save_memory()

    def search_memory(self, keyword: str) -> Dict[str, Any]:
        """
        Searches memory for entries containing the given keyword.

        Args:
            keyword (str): The keyword to search for.

        Returns:
            dict: A dictionary of matching memory entries.
        """
        return {
            key: value
            for key, value in self.memory_store.items()
            if keyword.lower() in str(value).lower()
        }

    def as_summary(self) -> str:
        """
        Provides a summary of the stored memory for reporting.

        Returns:
            str: A formatted string summarizing the long-term memory.
        """
        summary = "\n".join(
            [f"{key}: {value}" for key, value in self.memory_store.items()]
        )
        return f"Long-Term Memory Summary:\n{summary}" if summary else "Memory is empty."

    def as_dict(self) -> Dict[str, Any]:
        """
        Returns the memory store as a dictionary.

        Returns:
            dict: The memory store.
        """
        return self.memory_store


if __name__ == "__main__":
    # Example usage
    ltm = LongTermMemory()

    # Add memory entries
    ltm.add_memory("AI trends", "Transformers are dominating the AI landscape.")
    ltm.add_memory("Quantum Computing", "Potential game changer for cryptography.")

    # Retrieve a specific memory
    print("Memory for 'AI trends':", ltm.get_memory("AI trends"))

    # List all memory keys
    print("All Memory Keys:", ltm.list_memory_keys())

    # Search memory
    print("Search Results:", ltm.search_memory("cryptography"))

    # Summary
    print(ltm.as_summary())

    # Clear memory
    ltm.clear_memory()
    print("After Clearing Memory:", ltm.list_memory_keys())
