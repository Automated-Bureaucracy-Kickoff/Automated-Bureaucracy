class AgentStateManager:
    """
    Manages and tracks the state of agents.
    """

    def __init__(self):
        self.agent_states = {}

    def set_state(self, agent_name: str, state: str):
        """
        Sets the state of an agent.
        """
        self.agent_states[agent_name] = state

    def get_state(self, agent_name: str) -> str:
        """
        Retrieves the state of an agent.
        """
        return self.agent_states.get(agent_name, "unknown")

    def reset_state(self, agent_name: str):
        """
        Resets the state of an agent to default.
        """
        if agent_name in self.agent_states:
            self.agent_states[agent_name] = "idle"
