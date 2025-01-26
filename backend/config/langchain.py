import os
import json


class LangChainConfig:
    """
    Configuration class for LangChain-specific settings.
    """

    def __init__(self, config_file: str = "langchain_config.json"):
        """
        Initialize the LangChainConfig class.

        Args:
            config_file (str): Path to the LangChain configuration file (default: "langchain_config.json").
        """
        self.config_file = config_file
        self.config = self._load_config()

    def _load_config(self) -> dict:
        """
        Load the LangChain configuration from a JSON file.

        Returns:
            dict: Configuration data.
        """
        if not os.path.exists(self.config_file):
            raise FileNotFoundError(f"Configuration file '{self.config_file}' not found.")

        try:
            with open(self.config_file, "r", encoding="utf-8") as file:
                return json.load(file)
        except json.JSONDecodeError as e:
            raise ValueError(f"Error decoding JSON in configuration file '{self.config_file}': {e}")

    def get(self, key: str, default=None):
        """
        Retrieve a specific configuration value.

        Args:
            key (str): The key for the configuration value.
            default: The default value to return if the key is not found.

        Returns:
            The value associated with the key or the default value.
        """
        return self.config.get(key, default)

    def get_all(self) -> dict:
        """
        Retrieve all LangChain configuration values.

        Returns:
            dict: All configuration data.
        """
        return self.config


# Example usage
if __name__ == "__main__":
    # Example configuration file path
    example_config_file = "langchain_config.json"

    # Sample content of `langchain_config.json`
    """
    {
        "default_model": "gpt-4",
        "default_temperature": 0.7,
        "default_tools": ["search", "notepad"],
        "tool_timeout": 30,
        "llm_max_tokens": 1000
    }
    """

    # Initialize LangChainConfig
    langchain_config = LangChainConfig(config_file=example_config_file)

    # Retrieve specific values
    default_model = langchain_config.get("default_model", "gpt-3.5")
    temperature = langchain_config.get("default_temperature", 0.5)

    print(f"Default Model: {default_model}")
    print(f"Default Temperature: {temperature}")

    # Retrieve all configurations
    all_config = langchain_config.get_all()
    print("All LangChain Configurations:", all_config)
