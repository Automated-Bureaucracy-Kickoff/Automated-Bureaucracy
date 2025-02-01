import os
import json


class Settings:
    """
    Centralized settings loader for the application.
    """

    def __init__(self, secrets_file: str = "config/secrets.json", default_env: str = "development"):
        """
        Initializes the Settings class.

        Args:
            secrets_file (str): Path to the secrets JSON file.
            default_env (str): Default environment to load settings for (default: "development").
        """
        self.environment = os.getenv("APP_ENV", default_env)
        self.secrets_file = secrets_file
        self.secrets = self._load_secrets()

    def _load_secrets(self) -> dict:
        """
        Loads sensitive data (e.g., API keys, system prompts) from a secrets JSON file.

        Returns:
            dict: Secrets data.
        """
        if not os.path.exists(self.secrets_file):
            raise FileNotFoundError(f"Secrets file '{self.secrets_file}' not found.")

        try:
            with open(self.secrets_file, "r", encoding="utf-8") as file:
                return json.load(file)
        except json.JSONDecodeError as e:
            raise ValueError(f"Error decoding JSON in secrets file '{self.secrets_file}': {e}")

    def get(self, key: str, default=None):
        """
        Retrieve a configuration value from environment variables or secrets file.

        Args:
            key (str): Configuration key.
            default: Default value if the key is not found.

        Returns:
            Value from the environment or secrets file, or the default value.
        """
        return os.getenv(key, self.secrets.get(key, default))

    def get_all(self) -> dict:
        """
        Retrieve all configuration settings, merging environment variables and secrets.

        Returns:
            dict: All settings.
        """
        config = self.secrets.copy()
        for key, value in os.environ.items():
            if key in config:
                config[key] = value
        return config


# Example Usage
if __name__ == "__main__":
    settings = Settings()

    # Access specific configurations
    openai_api_key = settings.get("openai_api_key")
    tavily_api_key = settings.get("tavily_api_key")
    system_prompt = settings.get("system_prompt", "Default system prompt")

    print(f"Environment: {settings.environment}")
    print(f"OpenAI API Key: {openai_api_key}")
    print(f"System Prompt: {system_prompt}")

    # Retrieve all settings
    all_settings = settings.get_all()
    print("All Settings:", all_settings)
