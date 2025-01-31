import os
import json
from dotenv import load_dotenv

class ConfigLoader:
    """
    Utility class for loading configuration settings from environment variables or a JSON config file.
    """

    def __init__(self, config_file=None):
        """
        Initialize the ConfigLoader.

        Args:
            config_file (str): Path to the JSON configuration file (optional).
        """
        self.config_file = config_file

        # Load environment variables from a .env file if it exists
        load_dotenv()

        # Load configuration from file if provided
        self.config_data = {}
        if self.config_file:
            self._load_config_file()

    def _load_config_file(self):
        """
        Load configuration from the specified JSON file.
        """
        if not os.path.exists(self.config_file):
            raise FileNotFoundError(f"Configuration file '{self.config_file}' not found.")
        
        try:
            with open(self.config_file, "r") as file:
                self.config_data = json.load(file)
        except json.JSONDecodeError as e:
            raise ValueError(f"Error decoding JSON in configuration file '{self.config_file}': {e}")

    def get(self, key, default=None):
        """
        Retrieve a configuration value.

        Args:
            key (str): The key of the configuration setting.
            default: Default value if the key is not found.

        Returns:
            The value associated with the key or the default value.
        """
        # Check environment variables first
        if key in os.environ:
            return os.environ[key]
        
        # Check configuration file
        return self.config_data.get(key, default)

    def get_all(self):
        """
        Retrieve all configuration data.

        Returns:
            dict: All configuration settings from both environment variables and the config file.
        """
        combined_config = {**self.config_data, **os.environ}
        return combined_config

# Example usage
if __name__ == "__main__":
    # Initialize with optional config file
    config_loader = ConfigLoader(config_file="config.json")

    # Access a specific configuration setting
    openai_key = config_loader.get("OPENAI_API_KEY", "default_key")
    print(f"OpenAI API Key: {openai_key}")

    # Access all configurations
    all_configs = config_loader.get_all()
    print(f"All Configurations: {all_configs}")
