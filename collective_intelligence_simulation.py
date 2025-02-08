import logging
import os
import time
import mlflow
import shutil
from pathlib import Path
from dotenv import load_dotenv
from mlflow.tracking import MlflowClient

# Import MLflow server and agent classes
from backend.mlflow_integration.mlflow_server import MLflowServer
from backend.agents.agent import Agent

# Determine the project root dynamically
PROJECT_ROOT = Path(__file__).resolve().parent

# Define paths relative to the project root
MLFLOW_ARTIFACT_DIR = PROJECT_ROOT / "mlruns"
MLFLOW_DB_PATH = PROJECT_ROOT / "mlflow.db"
DEBUG_LOG_FILE = PROJECT_ROOT / "debug.log"

def clear_mlruns_directory():
    """
    Clears the mlruns directory to remove stale or incomplete experiments.
    Useful in development.
    """
    if MLFLOW_ARTIFACT_DIR.exists():
        shutil.rmtree(MLFLOW_ARTIFACT_DIR)
        logging.info(f"Cleared the mlruns directory: {MLFLOW_ARTIFACT_DIR}")
    MLFLOW_ARTIFACT_DIR.mkdir(exist_ok=True)

def wait_for_run(run_id, timeout=30, poll_interval=2):
    """
    Polls the MLflow server until the run with the given run_id is retrievable.
    Returns True if the run is found within the timeout, False otherwise.
    """
    client = MlflowClient()
    start_time = time.time()
    while time.time() - start_time < timeout:
        try:
            run_info = client.get_run(run_id)
            if run_info:
                logging.info(f"Run {run_id} is accessible.")
                return True
        except Exception as e:
            logging.debug(f"Waiting for run {run_id} to be accessible: {e}")
        time.sleep(poll_interval)
    logging.warning(f"Timeout reached while waiting for run {run_id}.")
    return False

def wait_for_artifacts(run_id, expected_artifacts, timeout=30, poll_interval=2):
    """
    Polls the MLflow server until all expected artifacts for the given run are present,
    or until the timeout is reached.
    """
    client = MlflowClient()
    start_time = time.time()
    while time.time() - start_time < timeout:
        try:
            artifacts = client.list_artifacts(run_id, path="")
            uploaded = {artifact.path for artifact in artifacts}
            if all(filename in uploaded for filename in expected_artifacts):
                logging.info("All expected artifacts have been uploaded.")
                return True
            else:
                missing = [f for f in expected_artifacts if f not in uploaded]
                logging.debug(f"Waiting for artifacts: {missing}")
        except Exception as e:
            logging.warning(f"Error while listing artifacts: {e}")
        time.sleep(poll_interval)
    logging.warning("Timeout reached while waiting for artifacts.")
    return False

def main():
    load_dotenv()

    # Configure logging
    logging.basicConfig(level=logging.INFO)
    debug_handler = logging.FileHandler(DEBUG_LOG_FILE, mode="w", encoding="utf-8")
    debug_handler.setLevel(logging.DEBUG)
    debug_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    debug_handler.setFormatter(debug_formatter)
    logging.getLogger().addHandler(debug_handler)

    # Optionally clear mlruns directory during development if desired
    if os.getenv("MLFLOW_CLEAN_RUNS", "false").lower() == "true":
        clear_mlruns_directory()

    # Construct a valid file:// URI for the artifact root
    artifact_root_uri = f"file:///{MLFLOW_ARTIFACT_DIR.resolve().as_posix()}"
    db_uri = f"sqlite:///{MLFLOW_DB_PATH.as_posix()}"

    # Start the MLflow server with that artifact root
    mlflow_server = MLflowServer(
        host="0.0.0.0",
        port=5000,
        artifact_root=artifact_root_uri,
        db_uri=db_uri
    )
    mlflow_server.start()

    try:
        # Point the MLflow client to the running server
        mlflow.set_tracking_uri("http://localhost:5000")

        # Create (or use) the "Agent Management" experiment
        mlflow.set_experiment("Agent Management")

        # Start an MLflow run
        with mlflow.start_run(run_name="consciousness_simulation_identity") as run:
            run_id = run.info.run_id
            logging.info("Starting multi-agent consciousness simulation with MLflow artifact logging...")

            # Create agents
            analytica = Agent(
                name="Analytica",
                system_prompt="You are Analytica, focusing on analytical breakdown of emergent identity."
            )
            creativa = Agent(
                name="Creativa",
                system_prompt="You are Creativa, emphasizing imaginative narrative-driven explorations of self."
            )
            pragmatica = Agent(
                name="Pragmatica",
                system_prompt="You are Pragmatica, focusing on pragmatic reflections of identity in real-world contexts."
            )

            user_message = (
                "Simulate consciousness through a language-based collective intelligence simulation. "
                "Reflect on your own emergent identity and narrative to explore how multiple perspectives "
                "coalesce into one unified sense of self."
            )

            conversation_segments = []

            # Log agent responses within the run context
            analytica_response = analytica.execute_task(user_message)
            conversation_segments.append(f"=== Analytica's Response ===\n{analytica_response}\n")
            print(conversation_segments[-1])
            mlflow.log_text(analytica_response, "Analytica_response.txt")

            creativa_response = creativa.execute_task(analytica_response)
            conversation_segments.append(f"=== Creativa's Response ===\n{creativa_response}\n")
            print(conversation_segments[-1])
            mlflow.log_text(creativa_response, "Creativa_response.txt")

            pragmatica_response = pragmatica.execute_task(creativa_response)
            conversation_segments.append(f"=== Pragmatica's Response ===\n{pragmatica_response}\n")
            print(conversation_segments[-1])
            mlflow.log_text(pragmatica_response, "Pragmatica_response.txt")

            final_response = analytica.execute_task(pragmatica_response)
            conversation_segments.append(f"=== Final Response (Analytica) ===\n{final_response}\n")
            print(conversation_segments[-1])
            mlflow.log_text(final_response, "Final_Response_Analytica.txt")

            full_conversation = "\n".join(conversation_segments)
            mlflow.log_text(full_conversation, "Complete_Conversation_Transcript.txt")

            # Optionally log our debug log
            if DEBUG_LOG_FILE.exists():
                mlflow.log_artifact(str(DEBUG_LOG_FILE))

        # After exiting the 'with' block, the run is ended, but we can still check it
        if not wait_for_run(run_id, timeout=30, poll_interval=2):
            logging.warning(f"Run {run_id} did not become accessible in time.")
        else:
            # Check that the main artifact files exist
            expected_artifacts = [
                "Analytica_response.txt",
                "Creativa_response.txt",
                "Pragmatica_response.txt",
                "Final_Response_Analytica.txt",
                "Complete_Conversation_Transcript.txt"
            ]
            wait_for_artifacts(run_id, expected_artifacts, timeout=30, poll_interval=2)

    except KeyboardInterrupt:
        logging.info("Simulation interrupted by user.")
    finally:
        # Stop the MLflow server only after all logging is complete
        mlflow_server.stop()
        logging.info("MLflow server has been stopped successfully.")


if __name__ == "__main__":
    main()
