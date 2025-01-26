from .agent import Agent

class BureaucracyAgent(Agent):
    """
    A specialized agent for handling bureaucratic workflows and task prioritization.
    """

    def prioritize_tasks(self):
        """
        Example method to prioritize tasks based on predefined criteria.
        """
        if not self.memory.load_memory():
            return "No tasks to prioritize."

        # Mock prioritization logic
        tasks = sorted(self.memory.load_memory(), key=lambda t: len(t))
        return tasks

    def delegate_task(self, other_agent, task):
        """
        Delegates a task to another agent.
        """
        return other_agent.execute_task(task)
