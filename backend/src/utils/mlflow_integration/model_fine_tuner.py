import mlflow
from mlflow.pyfunc import PythonModel
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, f1_score, mean_squared_error
from typing import Dict, Any, Tuple, Callable
import pandas as pd


class ModelFineTuner:
    """
    Utility for fine-tuning machine learning models with MLflow integration.
    """

    def __init__(self, tracking_uri: str = "http://localhost:5000"):
        """
        Initialize the ModelFineTuner.

        Args:
            tracking_uri (str): URI for the MLflow tracking server.
        """
        mlflow.set_tracking_uri(tracking_uri)

    def load_data(self, data_path: str) -> pd.DataFrame:
        """
        Load dataset from a file.

        Args:
            data_path (str): Path to the data file.

        Returns:
            pd.DataFrame: Loaded dataset.
        """
        return pd.read_csv(data_path)

    def split_data(
        self, data: pd.DataFrame, target_column: str, test_size: float = 0.2
    ) -> Tuple[pd.DataFrame, pd.DataFrame, pd.Series, pd.Series]:
        """
        Split data into training and testing sets.

        Args:
            data (pd.DataFrame): Dataset to split.
            target_column (str): Column name for the target variable.
            test_size (float, optional): Proportion of the dataset to include in the test split. Defaults to 0.2.

        Returns:
            Tuple[pd.DataFrame, pd.DataFrame, pd.Series, pd.Series]: Training features, test features, training labels, test labels.
        """
        X = data.drop(columns=[target_column])
        y = data[target_column]
        return train_test_split(X, y, test_size=test_size, random_state=42)

    def log_metrics(self, run_id: str, metrics: Dict[str, float]) -> None:
        """
        Log evaluation metrics to MLflow.

        Args:
            run_id (str): ID of the MLflow run.
            metrics (dict): Dictionary of metrics to log.
        """
        for metric_name, metric_value in metrics.items():
            mlflow.log_metric(metric_name, metric_value)

    def fine_tune_model(
        self,
        model: Callable,
        train_features: pd.DataFrame,
        train_labels: pd.Series,
        val_features: pd.DataFrame,
        val_labels: pd.Series,
        hyperparameters: Dict[str, Any],
    ) -> Tuple[Any, Dict[str, float]]:
        """
        Fine-tune the model with the provided hyperparameters.

        Args:
            model (Callable): Model class or function to train.
            train_features (pd.DataFrame): Training features.
            train_labels (pd.Series): Training labels.
            val_features (pd.DataFrame): Validation features.
            val_labels (pd.Series): Validation labels.
            hyperparameters (dict): Dictionary of hyperparameters for model initialization.

        Returns:
            Tuple[Any, dict]: Trained model and evaluation metrics.
        """
        # Initialize and train the model
        trained_model = model(**hyperparameters)
        trained_model.fit(train_features, train_labels)

        # Make predictions
        predictions = trained_model.predict(val_features)

        # Calculate metrics
        metrics = {
            "accuracy": accuracy_score(val_labels, predictions),
            "f1_score": f1_score(val_labels, predictions, average="weighted"),
            "mse": mean_squared_error(val_labels, predictions),
        }

        return trained_model, metrics

    def track_model(
        self,
        model_name: str,
        trained_model: Any,
        hyperparameters: Dict[str, Any],
        metrics: Dict[str, float],
        artifacts: Dict[str, str] = None,
    ) -> str:
        """
        Track the fine-tuned model and its artifacts with MLflow.

        Args:
            model_name (str): Name of the model.
            trained_model (Any): Trained model instance.
            hyperparameters (dict): Hyperparameters used for training.
            metrics (dict): Evaluation metrics.
            artifacts (dict, optional): Dictionary of artifact paths to log. Defaults to None.

        Returns:
            str: ID of the MLflow run.
        """
        with mlflow.start_run() as run:
            # Log parameters, metrics, and model
            mlflow.log_params(hyperparameters)
            mlflow.log_metrics(metrics)
            mlflow.sklearn.log_model(trained_model, model_name)

            # Log additional artifacts if provided
            if artifacts:
                for artifact_name, artifact_path in artifacts.items():
                    mlflow.log_artifact(artifact_path, artifact_path=artifact_name)

            return run.info.run_id
