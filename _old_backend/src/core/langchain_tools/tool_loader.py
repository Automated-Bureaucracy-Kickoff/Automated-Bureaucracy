"""
Tool Loader

This module provides functionality to dynamically load and manage LangChain tools
within the Automated Bureaucracy system.
"""

from langchain.agents import Tool
from langchain.tools import BaseTool
from typing import List, Dict, Callable
import importlib
import logging

# Initialize logger
logger = logging.getLogger(__name__)


class ToolLoader:
    """
    ToolLoader is responsible for loading, managing, and registering tools dynamically.
    """

    def __init__(self):
        """
        Initializes the ToolLoader with an empty tool registry.
        """
        self.tool_registry: Dict[str, Tool] = {}

    def load_tool(self, name: str, func: Callable, description: str) -> Tool:
        """
        Loads a single tool and registers it in the tool registry.

        Args:
            name (str): Name of the tool.
            func (Callable): The function associated with the tool.
            description (str): Description of the tool's functionality.

        Returns:
            Tool: The LangChain Tool instance.
        """
        tool = Tool(name=name, func=func, description=description)
        self.tool_registry[name] = tool
        logger.info(f"Tool '{name}' loaded successfully.")
        return tool

    def load_tools_from_config(self, config: List[Dict[str, str]]) -> List[Tool]:
        """
        Loads multiple tools from a configuration.

        Args:
            config (List[Dict[str, str]]): List of tool configurations, where each entry contains:
                - `name`: Name of the tool.
                - `module`: Path to the module containing the tool function.
                - `function`: Name of the function to load.
                - `description`: Description of the tool.

        Returns:
            List[Tool]: A list of LangChain Tool instances.
        """
        tools = []
        for tool_config in config:
            try:
                module = importlib.import_module(tool_config["module"])
                func = getattr(module, tool_config["function"])
                tool = self.load_tool(
                    name=tool_config["name"],
                    func=func,
                    description=tool_config["description"],
                )
                tools.append(tool)
            except Exception as e:
                logger.error(
                    f"Failed to load tool '{tool_config['name']}': {str(e)}"
                )
        return tools

    def get_tool(self, name: str) -> Tool:
        """
        Retrieves a tool by its name.

        Args:
            name (str): Name of the tool.

        Returns:
            Tool: The LangChain Tool instance.

        Raises:
            KeyError: If the tool is not found in the registry.
        """
        if name not in self.tool_registry:
            raise KeyError(f"Tool '{name}' is not registered.")
        return self.tool_registry[name]

    def list_tools(self) -> List[str]:
        """
        Lists all registered tools.

        Returns:
            List[str]: Names of all registered tools.
        """
        return list(self.tool_registry.keys())


# Example usage
if __name__ == "__main__":
    # Initialize ToolLoader
    tool_loader = ToolLoader()

    # Example function for a tool
    def example_tool(input_text: str) -> str:
        return f"Processed input: {input_text}"

    # Load a tool manually
    tool_loader.load_tool(
        name="ExampleTool",
        func=example_tool,
        description="An example tool for demonstration purposes.",
    )

    # Example configuration for multiple tools
    tool_config = [
        {
            "name": "ExampleTool2",
            "module": "backend.langchain_tools.tools.example_module",
            "function": "example_function",
            "description": "Another example tool loaded dynamically.",
        }
    ]

    # Load tools from configuration
    tool_loader.load_tools_from_config(tool_config)

    # List registered tools
    print("Registered Tools:", tool_loader.list_tools())
