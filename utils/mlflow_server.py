import subprocess
import os
import logging
import time

class MLflowServer:
    """
    Manages the MLflow tracking server programmatically.
    """

    def __init__(self, host: str = "0.0.0.0", port: int = 5000, artifact_root: str = "./mlruns", db_uri: str = "sqlite:///mlflow.db"):
        """
        Initializes the MLflow server configuration.

        Args:
            host (str): The host for the MLflow server.
            port (int): The port for the MLflow server.
            artifact_root (str): The directory to store artifacts.
            db_uri (str): The URI for the backend store database.
        """
        self.host = host
        self.port = port
        self.artifact_root = artifact_root
        self.db_uri = db_uri
        self.process = None

    def start(self):
        """
        Starts the MLflow server in a subprocess.
        """
        try:
            logging.info("Starting MLflow server on %s:%d", self.host, self.port)
            self.process = subprocess.Popen(
                [
                    "mlflow", "server",
                    "--host", self.host,
                    "--port", str(self.port),
                    "--backend-store-uri", self.db_uri,
                    "--default-artifact-root", self.artifact_root
                ],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                universal_newlines=True
            )
            time.sleep(5)  # Allow time for the server to initialize
            logging.info("MLflow server started successfully.")
        except FileNotFoundError as e:
            logging.error("MLflow CLI not found. Ensure MLflow is installed and available in PATH: %s", e)
        except Exception as e:
            logging.error("Failed to start MLflow server: %s", e)

    def stop(self):
        """
        Stops the MLflow server.
        """
        if self.process and self.process.poll() is None:
            logging.info("Stopping MLflow server...")
            self.process.terminate()
            self.process.wait()
            logging.info("MLflow server stopped successfully.")

    def is_running(self):
        """
        Checks if the MLflow server is running.

        Returns:
            bool: True if the server is running, False otherwise.
        """
        return self.process is not None and self.process.poll() is None
