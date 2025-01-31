"""
authorization.py

Handles user authorization tasks, such as verifying roles and permissions for accessing specific resources.
"""

from typing import List, Dict
from authentication import Authentication, AuthenticationError


class AuthorizationError(Exception):
    """Custom exception for authorization errors."""
    pass


class Authorization:
    """
    Provides methods for managing user roles and permissions for resource access.
    """

    def __init__(self, role_permissions: Dict[str, List[str]]):
        """
        Initializes the Authorization class with predefined role permissions.

        Args:
            role_permissions (Dict[str, List[str]]): A dictionary mapping roles to their allowed actions.
        """
        self.role_permissions = role_permissions

    def verify_access(self, token: str, required_permissions: List[str]) -> bool:
        """
        Verify if a user has the required permissions based on their role.

        Args:
            token (str): The JWT token of the user.
            required_permissions (List[str]): The list of permissions required to access a resource.

        Returns:
            bool: True if the user has all required permissions, False otherwise.

        Raises:
            AuthorizationError: If the token is invalid, expired, or the user lacks permissions.
        """
        try:
            decoded_token = Authentication.verify_token(token)
            user_role = decoded_token.get("role")

            if not user_role:
                raise AuthorizationError("User role not found in token.")

            allowed_permissions = self.role_permissions.get(user_role, [])

            if not set(required_permissions).issubset(set(allowed_permissions)):
                raise AuthorizationError("User does not have the required permissions.")

            return True
        except AuthenticationError as e:
            raise AuthorizationError(f"Authentication error: {e}")

    def assign_role_to_user(self, user_id: str, role: str, user_database: Dict[str, Dict[str, str]]) -> None:
        """
        Assign a role to a user.

        Args:
            user_id (str): The unique identifier for the user.
            role (str): The role to assign.
            user_database (Dict[str, Dict[str, str]]): A dictionary containing user data, including roles.

        Raises:
            AuthorizationError: If the user is not found in the database.
        """
        if user_id not in user_database:
            raise AuthorizationError("User not found in the database.")

        user_database[user_id]["role"] = role

    def check_user_role(self, token: str) -> str:
        """
        Retrieve the role of a user from their token.

        Args:
            token (str): The JWT token of the user.

        Returns:
            str: The role of the user.

        Raises:
            AuthorizationError: If the token is invalid or the role is missing.
        """
        try:
            decoded_token = Authentication.verify_token(token)
            user_role = decoded_token.get("role")

            if not user_role:
                raise AuthorizationError("User role not found in token.")

            return user_role
        except AuthenticationError as e:
            raise AuthorizationError(f"Authentication error: {e}")


# Example Usage
if __name__ == "__main__":
    # Define roles and their permissions
    roles_permissions = {
        "admin": ["create", "read", "update", "delete"],
        "editor": ["create", "read", "update"],
        "viewer": ["read"],
    }

    # Mock user database
    user_db = {
        "user1": {"password": Authentication.hash_password("securepassword123"), "role": "admin"},
        "user2": {"password": Authentication.hash_password("mypassword456"), "role": "viewer"},
    }

    # Initialize Authorization
    auth = Authorization(role_permissions=roles_permissions)

    # Authenticate a user and get a token
    try:
        token = Authentication.create_token("user1")
        print(f"Generated token: {token}")

        # Verify user access
        if auth.verify_access(token, ["create", "read"]):
            print("Access granted.")
        else:
            print("Access denied.")

        # Check user role
        role = auth.check_user_role(token)
        print(f"User role: {role}")

    except AuthorizationError as e:
        print(f"Authorization failed: {e}")
