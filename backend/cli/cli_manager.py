import argparse
import logging
from backend.cli.utils.workflow_helper import WorkflowHelper
from backend.agents.multi_agent_manager import MultiAgentManager

logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s")


class CLIManager:
    def __init__(self):
        self.parser = argparse.ArgumentParser(description="CLI for Automated Bureaucracy")
        self.subparsers = self.parser.add_subparsers(dest="command", required=True)
        self._register_commands()

    def _register_commands(self):
        sp = self.subparsers
        sp.add_parser("simulate-collective-intelligence").set_defaults(func=self.simulate_collective_intelligence)

    def simulate_collective_intelligence(self, args):
        """
        Handles the default collective intelligence simulation.
        """
        logging.info("Starting simulation.")

        # Initialize MultiAgentManager
        manager = MultiAgentManager()

        # Define default agents
        default_agents = [
            {
                "name": "Analytica",
                "system_prompt": "You are an analytical assistant focused on logic, data, and systematic reasoning.",
                "openai_api_key": "your_openai_api_key",
                "tavily_api_key": "your_tavily_api_key",
                "mlflow_uri": "http://127.0.0.1:5000",
            },
            {
                "name": "Creativa",
                "system_prompt": "You are a creative assistant focused on imagination, ideas, and innovation.",
                "openai_api_key": "your_openai_api_key",
                "tavily_api_key": "your_tavily_api_key",
                "mlflow_uri": "http://127.0.0.1:5000",
            },
            {
                "name": "Pragmatica",
                "system_prompt": "You are a practical assistant focused on real-world applications and solutions.",
                "openai_api_key": "your_openai_api_key",
                "tavily_api_key": "your_tavily_api_key",
                "mlflow_uri": "http://127.0.0.1:5000",
            },
        ]

        # Register default agents
        for agent in default_agents:
            try:
                manager.create_agent(
                    name=agent["name"],
                    system_prompt=agent["system_prompt"],
                    openai_api_key=agent["openai_api_key"],
                    tavily_api_key=agent["tavily_api_key"],
                    mlflow_uri=agent["mlflow_uri"],
                )
                logging.info(f"Registered agent: {agent['name']}")
            except Exception as e:
                logging.error(f"Failed to register agent {agent['name']}: {e}")

        # Run the default collective intelligence simulation
        try:
            logging.info("Starting default collective intelligence simulation...")
            manager.run_simulation("Default simulation", 5, debug_mode=True)
        except Exception as e:
            logging.error(f"Simulation failed: {e}")

    def run(self):
        """
        Parses command-line arguments and runs the appropriate command.
        """
        args = self.parser.parse_args()
        if hasattr(args, "func"):
            args.func(args)
        else:
            self.parser.print_help()


if __name__ == "__main__":
    CLIManager().run()
