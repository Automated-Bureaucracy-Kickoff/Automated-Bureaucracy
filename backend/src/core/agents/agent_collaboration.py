from .multi_agent_manager import MultiAgentManager

class AgentCollaboration:
    """
    Facilitates collaboration between multiple agents.
    """

    def __init__(self, manager: MultiAgentManager):
        self.manager = manager

    def share_task(self, from_agent: str, to_agent: str, task: str) -> str:
        """
        Shares a task from one agent to another.
        """
        sender = self.manager.get_agent(from_agent)
        receiver = self.manager.get_agent(to_agent)

        if not sender or not receiver:
            return "One or both agents not found."

        # Example logic: receiver adds the task
        result = receiver.execute_task(task)
        return f"Task shared from {from_agent} to {to_agent}. Result: {result}"
