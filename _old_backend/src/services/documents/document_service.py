"""
Document Service Module
Provides functionality for managing documents in the Automated Bureaucracy system.
"""

from typing import Dict, List, Optional
from backend.security.document.document_access_control import DocumentAccessControl


class DocumentService:
    """
    A service for managing documents, including creation, retrieval, updates, and access control.
    """

    def __init__(self):
        """
        Initialize the DocumentService with a DocumentAccessControl instance.
        """
        self.documents: Dict[str, Dict] = {}
        self.access_control = DocumentAccessControl()

    def create_document(self, doc_id: str, content: str, owner: str) -> str:
        """
        Create a new document.

        Args:
            doc_id (str): The unique identifier for the document.
            content (str): The content of the document.
            owner (str): The user who owns the document.

        Returns:
            str: Confirmation message for document creation.
        """
        if doc_id in self.documents:
            raise ValueError(f"Document with ID {doc_id} already exists.")
        
        self.documents[doc_id] = {
            "content": content,
            "owner": owner,
            "permissions": {owner: "read_write"}
        }
        self.access_control.grant_access(doc_id, owner)
        return f"Document {doc_id} created successfully."

    def get_document(self, doc_id: str, user: str) -> Optional[Dict]:
        """
        Retrieve a document if the user has access.

        Args:
            doc_id (str): The document's unique identifier.
            user (str): The user requesting the document.

        Returns:
            Optional[Dict]: The document content and metadata.
        """
        if not self.access_control.has_access(doc_id, user):
            raise PermissionError(f"User {user} does not have access to document {doc_id}.")
        
        document = self.documents.get(doc_id)
        if not document:
            raise ValueError(f"Document {doc_id} not found.")
        
        return {
            "doc_id": doc_id,
            "content": document["content"],
            "owner": document["owner"]
        }

    def update_document(self, doc_id: str, user: str, new_content: str) -> str:
        """
        Update a document's content.

        Args:
            doc_id (str): The document's unique identifier.
            user (str): The user making the update.
            new_content (str): The new content for the document.

        Returns:
            str: Confirmation message for the update.
        """
        if not self.access_control.has_access(doc_id, user):
            raise PermissionError(f"User {user} does not have write access to document {doc_id}.")
        
        if doc_id not in self.documents:
            raise ValueError(f"Document {doc_id} not found.")
        
        self.documents[doc_id]["content"] = new_content
        return f"Document {doc_id} updated successfully."

    def delete_document(self, doc_id: str, user: str) -> str:
        """
        Delete a document.

        Args:
            doc_id (str): The document's unique identifier.
            user (str): The user attempting the deletion.

        Returns:
            str: Confirmation message for the deletion.
        """
        if doc_id not in self.documents:
            raise ValueError(f"Document {doc_id} not found.")
        
        if self.documents[doc_id]["owner"] != user:
            raise PermissionError(f"User {user} is not authorized to delete document {doc_id}.")
        
        del self.documents[doc_id]
        self.access_control.revoke_access(doc_id)
        return f"Document {doc_id} deleted successfully."

    def list_documents(self, user: str) -> List[str]:
        """
        List all documents the user has access to.

        Args:
            user (str): The user requesting the document list.

        Returns:
            List[str]: A list of document IDs.
        """
        accessible_docs = [
            doc_id for doc_id in self.documents
            if self.access_control.has_access(doc_id, user)
        ]
        return accessible_docs
