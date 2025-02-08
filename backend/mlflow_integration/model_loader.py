import mlflow
import mlflow.pyfunc
from mlflow.tracking import MlflowClient
from typing import Any, List, Dict


class ModelLoader:
    """
    Utility for loading and using models tracked in MLflow.
    """

    def __init__(self, tracking_uri: str = "http://localhost:5000") -> None:
        """
        Initialize the ModelLoader.

        Args:
            tracking_uri (str): URI for the MLflow tracking server.
        """
        mlflow.set_tracking_uri(tracking_uri)

    def load_model(self, model_uri: str) -> Any:
        """
        Load a model from MLflow using its URI.

        Args:
            model_uri (str): URI of the model to load (e.g., 'models:/model_name/version').

        Returns:
            Any: Loaded model instance.
        """
        try:
            model = mlflow.pyfunc.load_model(model_uri)
            return model
        except Exception as e:
            raise RuntimeError(f"Failed to load model from {model_uri}: {e}")

    def predict(self, model: Any, input_data: Any) -> Any:
        """
        Use the loaded model to make predictions.

        Args:
            model (Any): Loaded model instance.
            input_data (Any): Input data for prediction (format depends on the model).

        Returns:
            Any: Predictions made by the model.
        """
        try:
            return model.predict(input_data)
        except Exception as e:
            raise RuntimeError(f"Prediction failed: {e}")

    def list_registered_models(self) -> List[str]:
        """
        List all registered models in the MLflow tracking server.

        Returns:
            List[str]: A list of registered model names.
        """
        try:
            client = MlflowClient()
            models = client.list_registered_models()
            return [model.name for model in models]
        except Exception as e:
            raise RuntimeError(f"Failed to list registered models: {e}")

    def get_model_version_info(self, model_name: str, version: str) -> Dict[str, Any]:
        """
        Get information about a specific model version.

        Args:
            model_name (str): Name of the model.
            version (str): Version identifier of the model.

        Returns:
            Dict[str, Any]: Details about the model version.
        """
        try:
            client = MlflowClient()
            version_info = client.get_model_version(model_name, version)
            return {
                "name": version_info.name,
                "version": version_info.version,
                "status": version_info.status,
                "description": version_info.description,
                "run_id": version_info.run_id,
                "source": version_info.source,
            }
        except Exception as e:
            raise RuntimeError(f"Failed to get model version info: {e}")

    def transition_model_stage(self, model_name: str, version: str, stage: str) -> None:
        """
        Transition a model version to a specific stage (e.g., 'Staging', 'Production').

        Args:
            model_name (str): Name of the model.
            version (str): Version identifier of the model.
            stage (str): Target stage to transition to.

        Raises:
            RuntimeError: If the stage transition fails.
        """
        try:
            client = MlflowClient()
            client.transition_model_version_stage(
                name=model_name, version=version, stage=stage
            )
        except Exception as e:
            raise RuntimeError(
                f"Failed to transition model {model_name} version {version} to stage {stage}: {e}"
            )
