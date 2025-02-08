import mlflow
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, f1_score, mean_squared_error
from typing import Dict, Any, Tuple, Callable
import pandas as pd


class ModelFineTuner:
    """
    Utility for fine-tuning machine learning models with MLflow integration.
    """

    def __init__(self, tracking_uri: str = "http://localhost:5000") -> None:
        """
        Initialize the ModelFineTuner.

        Args:
            tracking_uri (str): URI for the MLflow tracking server.
        """
        mlflow.set_tracking_uri(tracking_uri)

    def load_data(self, data_path: str) -> pd.DataFrame:
        """
        Load a dataset from a CSV file.

        Args:
            data_path (str): Path to the CSV file containing the dataset.

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
            target_column (str): Name of the target variable column.
            test_size (float, optional): Proportion of data to use for testing. Defaults to 0.2.

        Returns:
            Tuple[pd.DataFrame, pd.DataFrame, pd.Series, pd.Series]:
                Training features, testing features, training labels, and testing labels.
        """
        X = data.drop(columns=[target_column])
        y = data[target_column]
        return train_test_split(X, y, test_size=test_size, random_state=42)

    def log_metrics(self, run_id: str, metrics: Dict[str, float]) -> None:
        """
        Log evaluation metrics to MLflow.

        Args:
            run_id (str): ID of the MLflow run.
            metrics (Dict[str, float]): Dictionary of metrics to log.
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

        Note:
            The current implementation assumes a classification task. For regression tasks,
            consider adjusting the metrics accordingly.

        Args:
            model (Callable): A model class or function that returns an untrained model instance.
            train_features (pd.DataFrame): Features for training.
            train_labels (pd.Series): Labels for training.
            val_features (pd.DataFrame): Features for validation.
            val_labels (pd.Series): Labels for validation.
            hyperparameters (Dict[str, Any]): Hyperparameters for initializing the model.

        Returns:
            Tuple[Any, Dict[str, float]]: The trained model and a dictionary of evaluation metrics.
        """
        trained_model = model(**hyperparameters)
        trained_model.fit(train_features, train_labels)

        predictions = trained_model.predict(val_features)
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
            model_name (str): Name under which to log the model.
            trained_model (Any): The trained model instance.
            hyperparameters (Dict[str, Any]): Hyperparameters used for training.
            metrics (Dict[str, float]): Evaluation metrics.
            artifacts (Dict[str, str], optional): A dictionary mapping artifact names to file paths.

        Returns:
            str: ID of the MLflow run.
        """
        with mlflow.start_run() as run:
            mlflow.log_params(hyperparameters)
            mlflow.log_metrics(metrics)
            # Assumes a scikit-learn model; adjust as needed for other model types.
            mlflow.sklearn.log_model(trained_model, model_name)

            if artifacts:
                for artifact_name, artifact_path in artifacts.items():
                    mlflow.log_artifact(artifact_path, artifact_path=artifact_name)

            return run.info.run_id
