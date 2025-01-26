"""
authentication.py

Handles user authentication tasks such as verifying credentials and managing authentication tokens.
"""

from typing import Optional
import hashlib
import jwt
from datetime import datetime, timedelta
from ..config.settings import get_secret_key

# Secret key for JWT encoding/decoding
SECRET_KEY = get_secret_key()

# Default token expiration time in minutes
TOKEN_EXPIRATION_MINUTES = 60


class AuthenticationError(Exception):
    """Custom exception for authentication errors."""
    pass


class Authentication:
    """
    Provides methods for authenticating users and managing authentication tokens.
    """

    @staticmethod
    def hash_password(password: str) -> str:
        """
        Hash a password using SHA256 for secure storage.

        Args:
            password (str): The plain text password.

        Returns:
            str: The hashed password.
        """
        return hashlib.sha256(password.encode('utf-8')).hexdigest()

    @staticmethod
    def verify_password(plain_password: str, hashed_password: str) -> bool:
        """
        Verify that a plain text password matches its hashed counterpart.

        Args:
            plain_password (str): The plain text password.
            hashed_password (str): The hashed password.

        Returns:
            bool: True if the passwords match, False otherwise.
        """
        return Authentication.hash_password(plain_password) == hashed_password

    @staticmethod
    def create_token(user_id: str, expiration_minutes: Optional[int] = TOKEN_EXPIRATION_MINUTES) -> str:
        """
        Create a JWT token for the given user.

        Args:
            user_id (str): The unique identifier for the user.
            expiration_minutes (Optional[int]): The token's expiration time in minutes.

        Returns:
            str: The generated JWT token.
        """
        expiration_time = datetime.utcnow() + timedelta(minutes=expiration_minutes)
        payload = {
            "user_id": user_id,
            "exp": expiration_time,
        }
        return jwt.encode(payload, SECRET_KEY, algorithm="HS256")

    @staticmethod
    def verify_token(token: str) -> dict:
        """
        Verify and decode a JWT token.

        Args:
            token (str): The JWT token to verify.

        Returns:
            dict: The decoded payload.

        Raises:
            AuthenticationError: If the token is invalid or expired.
        """
        try:
            return jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        except jwt.ExpiredSignatureError:
            raise AuthenticationError("Token has expired.")
        except jwt.InvalidTokenError:
            raise AuthenticationError("Invalid token.")

    @staticmethod
    def authenticate_user(username: str, password: str, user_database: dict) -> str:
        """
        Authenticate a user against a user database.

        Args:
            username (str): The username of the user.
            password (str): The password of the user.
            user_database (dict): A dictionary of user credentials {username: hashed_password}.

        Returns:
            str: The JWT token for the authenticated user.

        Raises:
            AuthenticationError: If authentication fails.
        """
        if username not in user_database:
            raise AuthenticationError("User not found.")

        hashed_password = user_database[username]
        if not Authentication.verify_password(password, hashed_password):
            raise AuthenticationError("Invalid password.")

        return Authentication.create_token(username)
