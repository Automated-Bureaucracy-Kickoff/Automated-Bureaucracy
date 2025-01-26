import os
import json


class BureaucracyConfig:
    """
    Configuration class for bureaucracy-specific settings.
    """

    def __init__(self, config_file: str = "bureaucracy_config.json"):
        """
        Initialize the BureaucracyConfig class.

        Args:
            config_file (str): Path to the configuration file (default: "bureaucracy_config.json").
        """
        self.config_file = config_file
        self.config = self._load_config()

    def _load_config(self) -> dict:
        """
        Load the bureaucracy configuration from a JSON file.

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
        Retrieve all bureaucracy configuration values.

        Returns:
            dict: All configuration data.
        """
        return self.config


# Example usage
if __name__ == "__main__":
    # Assuming a JSON configuration file exists
    example_config_file = "bureaucracy_config.json"

    # Sample content of `bureaucracy_config.json`
    """
    {
        "default_agent_role": "Decision Maker",
        "workflow_timeout": 60,
        "approval_threshold": 0.8,
        "escalation_contact": "admin@bureaucracy.local"
    }
    """

    # Initialize BureaucracyConfig
    bureaucracy_config = BureaucracyConfig(config_file=example_config_file)

    # Retrieve specific values
    default_role = bureaucracy_config.get("default_agent_role", "Agent")
    timeout = bureaucracy_config.get("workflow_timeout", 30)

    print(f"Default Agent Role: {default_role}")
    print(f"Workflow Timeout: {timeout} minutes")

    # Retrieve all values
    all_config = bureaucracy_config.get_all()
    print("All Bureaucracy Configurations:", all_config)
