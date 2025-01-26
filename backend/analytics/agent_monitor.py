import datetime
from typing import Dict, Any, List
from ..agents.agent import Agent
from ..agents.multi_agent_manager import MultiAgentManager

class AgentMonitor:
    """
    Monitors agents, tracks their activities, and generates analytics.
    """

    def __init__(self, agent_manager: MultiAgentManager):
        """
        Initializes the AgentMonitor with a reference to the MultiAgentManager.

        Args:
            agent_manager (MultiAgentManager): Manages multiple agents.
        """
        self.agent_manager = agent_manager
        self.agent_logs: Dict[str, List[Dict[str, Any]]] = {}

    def log_activity(self, agent_name: str, activity: str):
        """
        Logs an agent's activity.

        Args:
            agent_name (str): Name of the agent.
            activity (str): Description of the activity.
        """
        timestamp = datetime.datetime.now().isoformat()
        if agent_name not in self.agent_logs:
            self.agent_logs[agent_name] = []
        self.agent_logs[agent_name].append({"timestamp": timestamp, "activity": activity})
        print(f"Activity logged for {agent_name}: {activity}")

    def get_agent_status(self, agent_name: str) -> Dict[str, Any]:
        """
        Retrieves the current status of an agent.

        Args:
            agent_name (str): Name of the agent.

        Returns:
            Dict[str, Any]: Current status of the agent.
        """
        agent = self.agent_manager.get_agent(agent_name)
        if not agent:
            return {"error": f"Agent {agent_name} not found."}
        return {
            "name": agent.name,
            "status": "active",  # Placeholder; could query AgentStateManager for real state
            "tasks_completed": len(agent.get_memory()),
            "last_activity": self.agent_logs.get(agent_name, [])[-1]["activity"] if self.agent_logs.get(agent_name) else "No activity logged",
        }

    def generate_summary(self) -> Dict[str, Any]:
        """
        Generates a summary report for all agents.

        Returns:
            Dict[str, Any]: Summary of agent statuses and activities.
        """
        summary = {
            "total_agents": len(self.agent_manager.list_agents()),
            "agent_details": [],
        }
        for agent_name, agent in self.agent_manager.list_agents().items():
            details = self.get_agent_status(agent_name)
            summary["agent_details"].append(details)
        return summary

    def detect_idle_agents(self, idle_threshold_minutes: int = 10) -> List[str]:
        """
        Detects agents that have been idle for longer than a threshold.

        Args:
            idle_threshold_minutes (int): The threshold for idle time in minutes.

        Returns:
            List[str]: Names of idle agents.
        """
        idle_agents = []
        now = datetime.datetime.now()
        for agent_name, logs in self.agent_logs.items():
            last_activity_time = datetime.datetime.fromisoformat(logs[-1]["timestamp"])
            if (now - last_activity_time).total_seconds() / 60 > idle_threshold_minutes:
                idle_agents.append(agent_name)
        return idle_agents
