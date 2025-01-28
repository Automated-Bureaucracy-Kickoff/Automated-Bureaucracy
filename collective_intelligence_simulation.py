# collective_intelligence_simulation.py (Refactored)
# Now only four total responses between three agents (Analytica, Creativa, Pragmatica)
# for a minimal proof of concept. Also removing the 'max_tokens' param in the agent.

import logging
import os
from dotenv import load_dotenv

from utils.mlflow_server import MLflowServer
from backend.agents.agent import Agent


def main():
    # 1) Load environment variables
    load_dotenv()
    logging.basicConfig(level=logging.INFO)

    # 2) Start the MLflow server
    mlflow_server = MLflowServer(
        host="0.0.0.0",      # or "localhost"
        port=5000,
        artifact_root="./mlruns",
        db_uri="sqlite:///mlflow.db"
    )
    mlflow_server.start()

    try:
        # Create three distinct agents with different system prompts.
        analytica = Agent(
            name="Analytica",
            system_prompt="You are Analytica, focusing on logic and data."  
        )
        creativa = Agent(
            name="Creativa",
            system_prompt="You are Creativa, focusing on imagination and new ideas."  
        )
        pragmatica = Agent(
            name="Pragmatica",
            system_prompt="You are Pragmatica, focusing on real-world solutions."  
        )

        # Minimal user message to get the conversation started:
        user_message = "We want to plan a new reading app. What's your initial take?"

        logging.info("Starting minimal multi-agent simulation...")

        # 1st agent response (Analytica)
        analytica_response = analytica.execute_task(user_message)
        print("\n=== Analytica's Response ===\n", analytica_response)

        # 2nd agent response (Creativa), using Analytica's output as input
        creativa_response = creativa.execute_task(analytica_response)
        print("\n=== Creativa's Response ===\n", creativa_response)

        # 3rd agent response (Pragmatica), using Creativa's output as input
        pragmatica_response = pragmatica.execute_task(creativa_response)
        print("\n=== Pragmatica's Response ===\n", pragmatica_response)

        # 4th and final agent response (Analytica again), using Pragmatica's output as input
        final_response = analytica.execute_task(pragmatica_response)
        print("\n=== Final Response (Analytica) ===\n", final_response)

    except KeyboardInterrupt:
        logging.info("Simulation interrupted by user.")
    finally:
        # Stop the MLflow server
        mlflow_server.stop()


if __name__ == "__main__":
    main()
