import logging
import mlflow
from typing import Dict, List, Any
from .agent import Agent

# Configure logging
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def ensure_experiment_exists(experiment_name: str) -> str:
    """
    Ensures that the specified MLflow experiment exists. If it does not, it creates it.

    Args:
        experiment_name (str): The name of the experiment to check or create.

    Returns:
        str: The ID of the experiment.
    """
    logging.debug("Ensuring experiment '%s' exists in MLflow.", experiment_name)
    experiment = mlflow.get_experiment_by_name(experiment_name)
    if experiment is None:
        logging.info("Experiment '%s' does not exist. Creating it.", experiment_name)
        mlflow.create_experiment(experiment_name)
    experiment_id = mlflow.get_experiment_by_name(experiment_name).experiment_id
    logging.debug("Experiment '%s' exists with ID '%s'.", experiment_name, experiment_id)
    return experiment_id

class MultiAgentManager:
    """
    Manages multiple intelligent agents, allowing creation, retrieval, updates, and execution of simulations.
    """

    def __init__(self):
        """
        Initializes the MultiAgentManager with an empty dictionary of agents.
        """
        self.agents: Dict[str, Agent] = {}

    def create_agent(self, name: str, system_prompt: str, openai_api_key: str, tavily_api_key: str, mlflow_uri: str) -> Agent:
        """
        Creates and registers a new agent.

        Args:
            name (str): The name of the agent.
            system_prompt (str): The system prompt defining the agent's behavior.
            openai_api_key (str): OpenAI API key.
            tavily_api_key (str): Tavily API key.
            mlflow_uri (str): URI for the MLflow server.

        Returns:
            Agent: The created agent instance.
        """
        logging.info("Creating agent '%s'.", name)
        try:
            agent = Agent(name, system_prompt, openai_api_key, tavily_api_key, mlflow_uri)
            self.agents[agent.name] = agent
            logging.debug("Agent '%s' created and registered successfully.", name)
            return agent
        except Exception as e:
            logging.error("Failed to create agent '%s': %s", name, e)
            raise

    def get_agent(self, name: str) -> Agent:
        """
        Retrieves an agent by name.

        Args:
            name (str): The name of the agent to retrieve.

        Returns:
            Agent: The retrieved agent instance or None if not found.
        """
        logging.debug("Retrieving agent '%s'.", name)
        return self.agents.get(name)

    def delete_agent(self, name: str) -> bool:
        """
        Deletes an agent by name.

        Args:
            name (str): The name of the agent to delete.

        Returns:
            bool: True if the agent was deleted, False otherwise.
        """
        logging.info("Deleting agent '%s'.", name)
        if name in self.agents:
            del self.agents[name]
            logging.debug("Agent '%s' deleted successfully.", name)
            return True
        logging.warning("Agent '%s' not found. Deletion failed.", name)
        return False

    def list_agents(self) -> Dict[str, Agent]:
        """
        Lists all registered agents.

        Returns:
            Dict[str, Agent]: A dictionary of agent names and their instances.
        """
        logging.debug("Listing all registered agents.")
        return self.agents

    def run_simulation(self, user_prompt: str, message_limit: int, debug_mode: bool = False) -> List[Dict[str, Any]]:
        """
        Runs a collective intelligence simulation across all registered agents.

        Args:
            user_prompt (str): The user-provided task or prompt.
            message_limit (int): The total message limit across all agents.
            debug_mode (bool): If True, enables debug logging.

        Returns:
            List[Dict]: Logs of the simulation.
        """
        logging.info("Starting collective intelligence simulation with user prompt: '%s'.", user_prompt)
        logs = []
        consecutive_failures = 0  # Track consecutive failures
        last_prompt = user_prompt  # Initial prompt
        agents = list(self.list_agents().values())

        if not agents:
            logging.error("No agents registered. Simulation cannot proceed.")
            raise RuntimeError("No agents registered for simulation.")

        # Ensure the MLflow experiment exists
        experiment_name = "Agent Management"
        try:
            experiment_id = ensure_experiment_exists(experiment_name)
            mlflow.set_experiment(experiment_name)
        except Exception as e:
            logging.error("Failed to set up MLflow experiment '%s': %s. Continuing without MLflow.", experiment_name, e)
            experiment_id = None

        try:
            with mlflow.start_run(run_name="collective_intelligence_simulation", experiment_id=experiment_id):
                for i in range(message_limit):
                    if consecutive_failures >= 3:
                        logging.error("Three consecutive task failures. Exiting simulation gracefully.")
                        break

                    agent = agents[i % len(agents)]  # Rotate through agents
                    logging.debug("Agent '%s' executing task.", agent.name)

                    try:
                        response = agent.execute_task(last_prompt)
                        logs.append({"agent": agent.name, "prompt": last_prompt, "response": response})
                        logging.info("Agent '%s' response: '%s'.", agent.name, response)
                        last_prompt = response  # Use response as the next prompt
                        consecutive_failures = 0  # Reset failure counter on success
                    except Exception as e:
                        consecutive_failures += 1
                        logging.error(
                            "Error during task execution for agent '%s': %s (Failure #%d)",
                            agent.name,
                            e,
                            consecutive_failures,
                        )

                logging.info("Simulation completed. Total messages exchanged: %d", len(logs))

        except Exception as e:
            logging.error("Error during simulation: %s", e)
            raise

        # Debug analysis summary
        analysis = {
            "total_messages_exchanged": len(logs),
            "successful_exchanges": [log for log in logs if "response" in log],
            "failed_exchanges": consecutive_failures,
            "agents_involved": [agent.name for agent in agents],
        }
        logging.debug("Simulation analysis: %s", analysis)

        return logs
