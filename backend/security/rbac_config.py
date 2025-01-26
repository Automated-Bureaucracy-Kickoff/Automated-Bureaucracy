"""
Role-Based Access Control (RBAC) Configuration Module

This module defines the roles, permissions, and access policies used throughout the system to enforce secure operations.
"""

from typing import Dict, List, Optional


class RBACConfig:
    """
    A class to manage Role-Based Access Control (RBAC) configurations.
    """

    def __init__(self):
        """
        Initialize the RBAC configuration with predefined roles and permissions.
        """
        self.roles: Dict[str, List[str]] = {}  # Maps roles to their permissions
        self.users: Dict[str, str] = {}  # Maps user IDs to their assigned roles

    def define_role(self, role: str, permissions: List[str]) -> None:
        """
        Define a new role with associated permissions.

        Args:
            role (str): The name of the role.
            permissions (List[str]): A list of permissions associated with the role.
        """
        self.roles[role] = permissions

    def assign_role(self, user_id: str, role: str) -> None:
        """
        Assign a role to a specific user.

        Args:
            user_id (str): The ID of the user.
            role (str): The role to assign to the user.

        Raises:
            ValueError: If the role does not exist.
        """
        if role not in self.roles:
            raise ValueError(f"Role '{role}' does not exist.")
        self.users[user_id] = role

    def remove_role(self, user_id: str) -> None:
        """
        Remove a role assignment from a user.

        Args:
            user_id (str): The ID of the user.
        """
        if user_id in self.users:
            del self.users[user_id]

    def check_permission(self, user_id: str, permission: str) -> bool:
        """
        Check if a user has a specific permission.

        Args:
            user_id (str): The ID of the user.
            permission (str): The permission to check.

        Returns:
            bool: True if the user has the permission, False otherwise.
        """
        role = self.users.get(user_id)
        if not role:
            return False
        return permission in self.roles.get(role, [])

    def list_roles(self) -> Dict[str, List[str]]:
        """
        List all roles and their permissions.

        Returns:
            Dict[str, List[str]]: A dictionary of roles and their associated permissions.
        """
        return self.roles

    def list_users(self) -> Dict[str, str]:
        """
        List all users and their assigned roles.

        Returns:
            Dict[str, str]: A dictionary mapping user IDs to their roles.
        """
        return self.users


# Example usage
if __name__ == "__main__":
    rbac = RBACConfig()

    # Define roles
    rbac.define_role("admin", ["create_user", "delete_user", "access_sensitive_data"])
    rbac.define_role("user", ["view_data", "update_profile"])

    # Assign roles to users
    rbac.assign_role("user_1", "admin")
    rbac.assign_role("user_2", "user")

    # Check permissions
    print(rbac.check_permission("user_1", "create_user"))  # True
    print(rbac.check_permission("user_2", "create_user"))  # False

    # List roles and users
    print(rbac.list_roles())
    print(rbac.list_users())
