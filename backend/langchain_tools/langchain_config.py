"""
LangChain Configuration

This module centralizes the configuration and initialization of LangChain components,
including tools, memory, chains, and language models used in the Automated Bureaucracy system.
"""

from langchain.llms import OpenAI
from langchain.memory import ConversationBufferMemory
from langchain.prompts import PromptTemplate
from langchain.agents import initialize_agent, Tool
import os

class LangChainConfig:
    """
    LangChain configuration class for managing tools, memory, and language models.
    """

    def __init__(self):
        """
        Initializes the LangChain configuration with default settings and tools.
        """
        self.openai_api_key = os.getenv("OPENAI_API_KEY")
        self.default_model = os.getenv("DEFAULT_MODEL", "gpt-4")
        self.memory = self.initialize_memory()

    def initialize_memory(self):
        """
        Initializes the default memory for LangChain agents.

        Returns:
            ConversationBufferMemory: A buffer memory instance.
        """
        return ConversationBufferMemory(memory_key="history", return_messages=True)

    def create_openai_llm(self):
        """
        Creates an OpenAI language model instance using environment settings.

        Returns:
            OpenAI: The initialized OpenAI model.
        """
        if not self.openai_api_key:
            raise ValueError("OpenAI API key is not set in environment variables.")
        return OpenAI(api_key=self.openai_api_key, model=self.default_model)

    def create_tools(self):
        """
        Defines and initializes the tools available for LangChain agents.

        Returns:
            list[Tool]: A list of LangChain Tool instances.
        """
        def notepad_tool(input_text):
            """
            Simulates a reflection notepad tool for storing agent thoughts.
            """
            return f"Reflection saved: {input_text}"

        def search_tool(query):
            """
            Placeholder for a search tool, simulating internet access.
            """
            return f"Search results for '{query}' (placeholder)."

        tools = [
            Tool(
                name="Notepad",
                func=notepad_tool,
                description="A tool for storing and reflecting on agent thoughts."
            ),
            Tool(
                name="Search",
                func=search_tool,
                description="Simulates internet search for real-time information."
            )
        ]
        return tools

    def initialize_agent(self):
        """
        Initializes a LangChain agent with configured tools, memory, and LLM.

        Returns:
            AgentExecutor: A LangChain agent instance.
        """
        llm = self.create_openai_llm()
        tools = self.create_tools()

        return initialize_agent(
            tools=tools,
            llm=llm,
            memory=self.memory,
            verbose=True
        )

    def get_prompt_template(self):
        """
        Creates a default prompt template for agents.

        Returns:
            PromptTemplate: A template instance for LangChain agents.
        """
        return PromptTemplate(
            input_variables=["context"],
            template=(
                "You are an advanced assistant. Respond to the following context:\n\n"
                "{context}"
            )
        )


# Singleton instance for LangChain configuration
langchain_config = LangChainConfig()

if __name__ == "__main__":
    # Example usage of LangChainConfig
    agent = langchain_config.initialize_agent()
    print("LangChain Agent initialized successfully.")
