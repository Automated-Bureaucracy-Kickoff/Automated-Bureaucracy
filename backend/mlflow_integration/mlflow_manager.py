import mlflow
from mlflow.tracking import MlflowClient
from typing import Dict, Any, Optional


class MLflowManager:
    """
    High-level manager for MLflow operations.

    Provides utilities for managing experiments, logging metrics, parameters, and artifacts.
    """

    def __init__(self, tracking_uri: str = "http://localhost:5000") -> None:
        """
        Initialize the MLflowManager with the MLflow tracking URI.

        Args:
            tracking_uri (str): URI for the MLflow tracking server.
        """
        mlflow.set_tracking_uri(tracking_uri)
        self.client = MlflowClient()

    def create_experiment(self, experiment_name: str) -> str:
        """
        Create a new experiment in MLflow.

        Args:
            experiment_name (str): Name of the experiment to create.

        Returns:
            str: ID of the created experiment.
        """
        experiment_id = self.client.create_experiment(experiment_name)
        return experiment_id

    def log_metrics(self, run_id: str, metrics: Dict[str, float]) -> None:
        """
        Log metrics to a specific run.

        Args:
            run_id (str): ID of the run to log metrics to.
            metrics (Dict[str, float]): A dictionary of metric names and their values.
        """
        for metric_name, metric_value in metrics.items():
            self.client.log_metric(run_id, metric_name, metric_value)

    def log_params(self, run_id: str, params: Dict[str, Any]) -> None:
        """
        Log parameters to a specific run.

        Args:
            run_id (str): ID of the run to log parameters to.
            params (Dict[str, Any]): A dictionary of parameter names and their values.
        """
        for param_name, param_value in params.items():
            self.client.log_param(run_id, param_name, param_value)

    def start_run(self, experiment_name: str, run_name: Optional[str] = None) -> str:
        """
        Start a new run in a specific experiment.

        Args:
            experiment_name (str): Name of the experiment to associate the run with.
            run_name (Optional[str], optional): Name of the run. Defaults to None.

        Returns:
            str: ID of the created run.
        """
        experiment = self.client.get_experiment_by_name(experiment_name)
        if not experiment:
            experiment_id = self.create_experiment(experiment_name)
        else:
            experiment_id = experiment.experiment_id

        tags = {"mlflow.runName": run_name} if run_name else None
        run = self.client.create_run(experiment_id=experiment_id, tags=tags)
        return run.info.run_id

    def end_run(self, run_id: str) -> None:
        """
        End a specific run.

        Args:
            run_id (str): ID of the run to end.
        """
        self.client.set_terminated(run_id)

    def log_artifact(self, run_id: str, file_path: str, artifact_path: Optional[str] = None) -> None:
        """
        Log an artifact to a specific run.

        Args:
            run_id (str): ID of the run to log the artifact to.
            file_path (str): Path to the file to log as an artifact.
            artifact_path (Optional[str], optional): Artifact path within the run. Defaults to None.
        """
        self.client.log_artifact(run_id, file_path, artifact_path)

    def get_run_details(self, run_id: str) -> Dict[str, Any]:
        """
        Retrieve details about a specific run.

        Args:
            run_id (str): ID of the run to retrieve details for.

        Returns:
            Dict[str, Any]: A dictionary containing run details including metrics, params, and artifacts.
        """
        run = self.client.get_run(run_id)
        return {
            "run_id": run.info.run_id,
            "experiment_id": run.info.experiment_id,
            "status": run.info.status,
            "metrics": run.data.metrics,
            "params": run.data.params,
            "artifacts": self.client.list_artifacts(run_id),
        }
