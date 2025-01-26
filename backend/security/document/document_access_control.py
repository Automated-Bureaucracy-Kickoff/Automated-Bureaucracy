"""
Document Access Control Module

This module provides functionality for managing access control policies for documents,
ensuring secure and authorized access to sensitive information.
"""

from typing import List, Dict


class DocumentAccessControl:
    """
    A class to manage document access control policies and enforce security rules.
    """

    def __init__(self):
        """
        Initialize the access control system with a policy database.
        """
        self.access_policies: Dict[str, List[str]] = {}  # Maps document IDs to a list of authorized users

    def add_policy(self, document_id: str, user_ids: List[str]):
        """
        Add or update an access policy for a specific document.

        Args:
            document_id (str): The ID of the document.
            user_ids (List[str]): List of user IDs authorized to access the document.
        """
        self.access_policies[document_id] = user_ids
        print(f"Access policy added for document {document_id}: {user_ids}")

    def remove_policy(self, document_id: str):
        """
        Remove the access policy for a specific document.

        Args:
            document_id (str): The ID of the document to remove the policy for.
        """
        if document_id in self.access_policies:
            del self.access_policies[document_id]
            print(f"Access policy removed for document {document_id}")
        else:
            print(f"No policy found for document {document_id}")

    def check_access(self, document_id: str, user_id: str) -> bool:
        """
        Check if a user has access to a specific document.

        Args:
            document_id (str): The ID of the document.
            user_id (str): The ID of the user requesting access.

        Returns:
            bool: True if the user has access, False otherwise.
        """
        authorized_users = self.access_policies.get(document_id, [])
        has_access = user_id in authorized_users
        print(f"Access check for user {user_id} on document {document_id}: {'Granted' if has_access else 'Denied'}")
        return has_access

    def list_policies(self) -> Dict[str, List[str]]:
        """
        List all access control policies.

        Returns:
            Dict[str, List[str]]: The current access policies.
        """
        return self.access_policies


# Example Usage
if __name__ == "__main__":
    access_control = DocumentAccessControl()

    # Add policies
    access_control.add_policy("doc_123", ["user_1", "user_2"])
    access_control.add_policy("doc_456", ["user_3"])

    # Check access
    access_control.check_access("doc_123", "user_1")  # Should print "Granted"
    access_control.check_access("doc_123", "user_3")  # Should print "Denied"

    # Remove policy
    access_control.remove_policy("doc_456")

    # List policies
    print("Current Policies:", access_control.list_policies())
