from typing import Dict
from .agent import Agent

class MultiAgentManager:
    """
    Manages multiple agents, allowing creation, retrieval, updates, and deletions.
    """

    def __init__(self):
        self.agents: Dict[str, Agent] = {}

    def create_agent(self, name: str, system_prompt: str, openai_api_key: str, tavily_api_key: str, mlflow_uri: str) -> Agent:
        """
        Creates and registers a new agent.
        """
        agent = Agent(name, system_prompt, openai_api_key, tavily_api_key, mlflow_uri)
        self.agents[agent.name] = agent
        return agent

    def get_agent(self, name: str) -> Agent:
        """
        Retrieves an agent by name.
        """
        return self.agents.get(name)

    def delete_agent(self, name: str) -> bool:
        """
        Deletes an agent by name.
        """
        if name in self.agents:
            del self.agents[name]
            return True
        return False

    def list_agents(self) -> Dict[str, Agent]:
        """
        Lists all agents.
        """
        return self.agents
