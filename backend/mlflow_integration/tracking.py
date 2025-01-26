import mlflow
from typing import Dict, Any


class TrackingManager:
    """
    Utility for managing MLflow tracking for experiments and runs.
    """

    def __init__(self, tracking_uri: str = "http://localhost:5000"):
        """
        Initialize the TrackingManager.

        Args:
            tracking_uri (str): URI for the MLflow tracking server.
        """
        mlflow.set_tracking_uri(tracking_uri)

    def set_experiment(self, experiment_name: str) -> str:
        """
        Set or create an experiment in MLflow.

        Args:
            experiment_name (str): Name of the experiment.

        Returns:
            str: Experiment ID.
        """
        try:
            experiment_id = mlflow.set_experiment(experiment_name)
            return experiment_id
        except Exception as e:
            raise RuntimeError(f"Failed to set experiment '{experiment_name}': {e}")

    def start_run(self, run_name: str = None, tags: Dict[str, str] = None) -> str:
        """
        Start a new MLflow run.

        Args:
            run_name (str, optional): Name of the run. Defaults to None.
            tags (Dict[str, str], optional): Tags to associate with the run. Defaults to None.

        Returns:
            str: Run ID.
        """
        try:
            run = mlflow.start_run(run_name=run_name, tags=tags)
            return run.info.run_id
        except Exception as e:
            raise RuntimeError(f"Failed to start run: {e}")

    def log_metrics(self, metrics: Dict[str, float]) -> None:
        """
        Log metrics to the current MLflow run.

        Args:
            metrics (Dict[str, float]): Metrics to log.

        Raises:
            RuntimeError: If logging fails.
        """
        try:
            mlflow.log_metrics(metrics)
        except Exception as e:
            raise RuntimeError(f"Failed to log metrics: {e}")

    def log_params(self, params: Dict[str, Any]) -> None:
        """
        Log parameters to the current MLflow run.

        Args:
            params (Dict[str, Any]): Parameters to log.

        Raises:
            RuntimeError: If logging fails.
        """
        try:
            mlflow.log_params(params)
        except Exception as e:
            raise RuntimeError(f"Failed to log parameters: {e}")

    def log_artifact(self, artifact_path: str, artifact_dir: str = None) -> None:
        """
        Log an artifact to the current MLflow run.

        Args:
            artifact_path (str): Path to the artifact file.
            artifact_dir (str, optional): Directory to store the artifact in MLflow. Defaults to None.

        Raises:
            RuntimeError: If logging fails.
        """
        try:
            mlflow.log_artifact(local_path=artifact_path, artifact_path=artifact_dir)
        except Exception as e:
            raise RuntimeError(f"Failed to log artifact '{artifact_path}': {e}")

    def end_run(self) -> None:
        """
        End the current MLflow run.

        Raises:
            RuntimeError: If ending the run fails.
        """
        try:
            mlflow.end_run()
        except Exception as e:
            raise RuntimeError(f"Failed to end run: {e}")

    def get_experiment_details(self, experiment_name: str) -> Dict[str, Any]:
        """
        Get details of a specific experiment by name.

        Args:
            experiment_name (str): Name of the experiment.

        Returns:
            Dict[str, Any]: Experiment details.
        """
        try:
            client = mlflow.MlflowClient()
            experiment = client.get_experiment_by_name(experiment_name)
            if not experiment:
                raise RuntimeError(f"Experiment '{experiment_name}' does not exist.")
            return {
                "experiment_id": experiment.experiment_id,
                "name": experiment.name,
                "artifact_location": experiment.artifact_location,
                "lifecycle_stage": experiment.lifecycle_stage,
            }
        except Exception as e:
            raise RuntimeError(f"Failed to get experiment details for '{experiment_name}': {e}")

    def list_runs(self, experiment_name: str) -> list:
        """
        List all runs for a specific experiment.

        Args:
            experiment_name (str): Name of the experiment.

        Returns:
            list: List of runs with details.
        """
        try:
            client = mlflow.MlflowClient()
            experiment = client.get_experiment_by_name(experiment_name)
            if not experiment:
                raise RuntimeError(f"Experiment '{experiment_name}' does not exist.")
            runs = client.search_runs(experiment_ids=[experiment.experiment_id])
            return [
                {
                    "run_id": run.info.run_id,
                    "status": run.info.status,
                    "start_time": run.info.start_time,
                    "end_time": run.info.end_time,
                }
                for run in runs
            ]
        except Exception as e:
            raise RuntimeError(f"Failed to list runs for experiment '{experiment_name}': {e}")
