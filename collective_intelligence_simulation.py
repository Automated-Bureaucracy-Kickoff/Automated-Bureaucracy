# collective_intelligence_simulation.py
#
# Updated to:
# - Use the consciousness-based user prompt.
# - Start the MLflow server, set the tracking URI to localhost:5000,
# - Start a single run and log all artifacts within that run,
# - Sleep briefly after the run completes so MLflow finalizes artifact uploads,
# - Then stop the MLflow server.
#
# This helps avoid "RESOURCE_DOES_NOT_EXIST" errors.

import logging
import os
import time
import mlflow
from dotenv import load_dotenv

from utils.mlflow_server import MLflowServer
from backend.agents.agent import Agent

def main():
    # 1) Load environment variables
    load_dotenv()

    # Configure logging
    logging.basicConfig(level=logging.INFO)

    # Additional debug logging to a file
    debug_handler = logging.FileHandler("debug.log", mode="w", encoding="utf-8")
    debug_handler.setLevel(logging.DEBUG)
    debug_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    debug_handler.setFormatter(debug_formatter)
    logging.getLogger().addHandler(debug_handler)

    # 2) Start the MLflow server
    mlflow_server = MLflowServer(
        host="0.0.0.0",  # or "localhost"
        port=5000,
        artifact_root="./mlruns",
        db_uri="sqlite:///mlflow.db"
    )
    mlflow_server.start()

    try:
        # Point the MLflow client to the local server you just started
        mlflow.set_tracking_uri("http://localhost:5000")

        # Create or use the "Agent Management" experiment
        mlflow.set_experiment("Agent Management")

        # Start run under that experiment
        with mlflow.start_run(run_name="consciousness_simulation_identity") as run:
            logging.info("Starting multi-agent consciousness simulation with MLflow artifact logging...")

            # Create three distinct agents
            analytica = Agent(
                name="Analytica",
                system_prompt="You are Analytica, focusing on analytical breakdown of emergent identity."
            )
            creativa = Agent(
                name="Creativa",
                system_prompt="You are Creativa, emphasizing imaginative, narrative-driven explorations of self."
            )
            pragmatica = Agent(
                name="Pragmatica",
                system_prompt="You are Pragmatica, focusing on pragmatic reflections of identity in real-world contexts."
            )

            # The user prompt about simulating consciousness & identity
            user_message = (
                "Simulate consciousness through a language-based collective intelligence simulation. "
                "Reflect on your own emergent identity and narrative to explore how multiple perspectives "
                "coalesce into one unified sense of self."
            )

            conversation_segments = []

            # (1) Analytica responds
            analytica_response = analytica.execute_task(user_message)
            conversation_segments.append(f"=== Analytica's Response ===\n{analytica_response}\n")
            print(conversation_segments[-1])
            mlflow.log_text(analytica_response, "Analytica_response.txt")

            # (2) Creativa responds
            creativa_response = creativa.execute_task(analytica_response)
            conversation_segments.append(f"=== Creativa's Response ===\n{creativa_response}\n")
            print(conversation_segments[-1])
            mlflow.log_text(creativa_response, "Creativa_response.txt")

            # (3) Pragmatica responds
            pragmatica_response = pragmatica.execute_task(creativa_response)
            conversation_segments.append(f"=== Pragmatica's Response ===\n{pragmatica_response}\n")
            print(conversation_segments[-1])
            mlflow.log_text(pragmatica_response, "Pragmatica_response.txt")

            # (4) Analytica final response
            final_response = analytica.execute_task(pragmatica_response)
            conversation_segments.append(f"=== Final Response (Analytica) ===\n{final_response}\n")
            print(conversation_segments[-1])
            mlflow.log_text(final_response, "Final_Response_Analytica.txt")

            # Combine all segments
            full_conversation = "\n".join(conversation_segments)
            mlflow.log_text(full_conversation, "Complete_Conversation_Transcript.txt")

            # Also log the debug.log
            if os.path.exists("debug.log"):
                mlflow.log_artifact("debug.log")

        # NOTE: The `with mlflow.start_run(...)` block automatically ends the run here

        # Let MLflow finalize artifact uploads
        logging.info("Pausing briefly to allow MLflow to finalize artifact uploads.")
        time.sleep(2)

    except KeyboardInterrupt:
        logging.info("Simulation interrupted by user.")

    finally:
        # Now that the run is done, we can safely stop the MLflow server
        mlflow_server.stop()
        logging.info("MLflow server has been stopped successfully.")

if __name__ == "__main__":
    main()
