"""
LangChain Tools Module

This module contains custom tools, chains, memory implementations, and prompts
to extend LangChain's functionality within the Automated Bureaucracy system.

Key Submodules:
- `chains`: Implements task-specific workflows using LangChain's Chain API.
- `memory`: Custom memory classes for context retention across tasks and workflows.
- `prompts`: Modular prompt templates to standardize interactions with agents.
- `tools`: Additional tools for agent capabilities, such as data reflection and API integrations.

Initialization:
The `langchain_tools` module provides a centralized API to configure and load all tools,
memory, chains, and prompts used by the backend.
"""

from .langchain_config import load_config
from .tool_loader import load_tools

__all__ = [
    "load_config",
    "load_tools",
]
