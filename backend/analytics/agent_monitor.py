import datetime
from abc import ABC, abstractmethod
from typing import Dict, Any, List, Optional

###############################################################################
# INTERFACES
###############################################################################

class IAgent(ABC):
    """
    Interface for an Agent.
    Each agent should implement a name property and a method to retrieve its memory.
    """

    @property
    @abstractmethod
    def name(self) -> str:
        """Return the name of the agent."""
        pass

    @abstractmethod
    def get_memory(self) -> List[Any]:
        """
        Retrieve a list representing the agent's memory or the tasks it has completed.
        Returns:
            List[Any]: A list of memory entries.
        """
        pass


class IMultiAgentManager(ABC):
    """
    Interface for a MultiAgentManager.
    This manager is responsible for retrieving individual agents and listing all agents.
    """

    @abstractmethod
    def get_agent(self, agent_name: str) -> Optional[IAgent]:
        """
        Retrieve a specific agent by name.
        Args:
            agent_name (str): The unique name of the agent.
        Returns:
            Optional[IAgent]: The agent instance if found, else None.
        """
        pass

    @abstractmethod
    def list_agents(self) -> Dict[str, IAgent]:
        """
        List all agents managed by the manager.
        Returns:
            Dict[str, IAgent]: A dictionary mapping agent names to agent instances.
        """
        pass


###############################################################################
# AGENT MONITOR IMPLEMENTATION
###############################################################################

class AgentMonitor:
    """
    Monitors agents by tracking their activities and generating analytics.
    
    This class logs agent activities with timestamps, retrieves the status of individual agents,
    generates summary reports across all agents, and detects idle agents based on configurable thresholds.
    """

    def __init__(self, agent_manager: IMultiAgentManager) -> None:
        """
        Initialize the AgentMonitor with a reference to a multi-agent manager.
        
        Args:
            agent_manager (IMultiAgentManager): An instance that manages multiple agents.
        """
        self.agent_manager = agent_manager

        # Dictionary to store activity logs for each agent.
        # Format: { agent_name: [ { "timestamp": str, "activity": str }, ... ] }
        self.agent_logs: Dict[str, List[Dict[str, Any]]] = {}

    def log_activity(self, agent_name: str, activity: str) -> None:
        """
        Log an activity for a specified agent.
        
        Args:
            agent_name (str): The name of the agent.
            activity (str): A description of the activity performed.
        """
        # Get the current timestamp in ISO format.
        timestamp = datetime.datetime.now().isoformat()

        # Initialize the log list for this agent if not present.
        if agent_name not in self.agent_logs:
            self.agent_logs[agent_name] = []

        # Append the log entry.
        self.agent_logs[agent_name].append({"timestamp": timestamp, "activity": activity})

        # Optionally, print or store the log externally.
        print(f"[{timestamp}] Activity logged for '{agent_name}': {activity}")

    def get_agent_status(self, agent_name: str) -> Dict[str, Any]:
        """
        Retrieve the current status of a specified agent.
        
        This method queries the agent manager for the agent and returns key metrics including:
        - Agent name.
        - A placeholder for agent status (e.g., "active").
        - Number of tasks or memory entries (as a proxy for tasks completed).
        - The last recorded activity.
        
        Args:
            agent_name (str): The name of the agent.
        
        Returns:
            Dict[str, Any]: A dictionary containing status details of the agent. If the agent is not found,
                            returns a dictionary with an error message.
        """
        # Retrieve the agent from the manager.
        agent = self.agent_manager.get_agent(agent_name)
        if not agent:
            return {"error": f"Agent '{agent_name}' not found."}

        # Determine the last activity if any logs exist.
        last_activity = "No activity logged"
        if self.agent_logs.get(agent_name):
            last_activity = self.agent_logs[agent_name][-1]["activity"]

        # Construct and return the agent's status.
        return {
            "name": agent.name,
            "status": "active",  # Placeholder; later integrate with a real AgentStateManager.
            "tasks_completed": len(agent.get_memory()),
            "last_activity": last_activity,
        }

    def generate_summary(self) -> Dict[str, Any]:
        """
        Generate a summary report for all agents managed by the system.
        
        The report includes the total number of agents and a detailed status for each.
        
        Returns:
            Dict[str, Any]: A summary dictionary containing the agent count and details.
        """
        summary: Dict[str, Any] = {
            "total_agents": 0,
            "agent_details": [],
        }

        # Retrieve the dictionary of all agents.
        agents = self.agent_manager.list_agents()
        summary["total_agents"] = len(agents)

        # Retrieve and include the status for each agent.
        for agent_name in agents:
            details = self.get_agent_status(agent_name)
            summary["agent_details"].append(details)

        return summary

    def detect_idle_agents(self, idle_threshold_minutes: int = 10) -> List[str]:
        """
        Detect agents that have been idle longer than a specified threshold.
        
        An agent is considered idle if the time since its last logged activity exceeds
        the threshold (in minutes).
        
        Args:
            idle_threshold_minutes (int, optional): The threshold in minutes to define idleness.
                                                     Defaults to 10 minutes.
        
        Returns:
            List[str]: A list of agent names that are idle.
        """
        idle_agents: List[str] = []
        now = datetime.datetime.now()

        # Iterate over each agent's activity logs.
        for agent_name, logs in self.agent_logs.items():
            if logs:
                # Get the timestamp of the last logged activity.
                last_activity_time = datetime.datetime.fromisoformat(logs[-1]["timestamp"])

                # Calculate the idle time in minutes.
                idle_duration = (now - last_activity_time).total_seconds() / 60
                if idle_duration > idle_threshold_minutes:
                    idle_agents.append(agent_name)

        return idle_agents


###############################################################################
# DUMMY IMPLEMENTATIONS FOR TESTING PURPOSES
###############################################################################

if __name__ == "__main__":
    # These dummy classes implement the interfaces defined above for demonstration and testing.
    
    class DummyAgent(IAgent):
        """
        A simple dummy implementation of an agent.
        """
        def __init__(self, name: str) -> None:
            self._name = name
            self._memory: List[Any] = []  # Placeholder for tasks or memory entries.
        
        @property
        def name(self) -> str:
            return self._name
        
        def get_memory(self) -> List[Any]:
            return self._memory

    class DummyMultiAgentManager(IMultiAgentManager):
        """
        A dummy multi-agent manager that maintains a collection of agents.
        """
        def __init__(self) -> None:
            self._agents: Dict[str, IAgent] = {}
        
        def add_agent(self, agent: IAgent) -> None:
            """Add a new agent to the manager."""
            self._agents[agent.name] = agent
        
        def get_agent(self, agent_name: str) -> Optional[IAgent]:
            return self._agents.get(agent_name)
        
        def list_agents(self) -> Dict[str, IAgent]:
            return self._agents

    # Instantiate the dummy manager and add two dummy agents.
    dummy_manager = DummyMultiAgentManager()
    agent_a = DummyAgent("AgentA")
    agent_b = DummyAgent("AgentB")
    dummy_manager.add_agent(agent_a)
    dummy_manager.add_agent(agent_b)

    # Create an instance of AgentMonitor with the dummy manager.
    monitor = AgentMonitor(dummy_manager)

    # Log some activities for the agents.
    monitor.log_activity("AgentA", "Started simulation workflow.")
    monitor.log_activity("AgentB", "Processing input data.")

    # Retrieve and display the status of AgentA.
    status_a = monitor.get_agent_status("AgentA")
    print("Status of AgentA:", status_a)

    # Generate and display a summary report of all agents.
    summary_report = monitor.generate_summary()
    print("Summary Report:", summary_report)

    # Detect and display idle agents with a threshold of 0 minutes (for demonstration).
    idle_agents = monitor.detect_idle_agents(idle_threshold_minutes=0)
    print("Idle Agents:", idle_agents)
