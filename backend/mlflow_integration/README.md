# MLflow Integration Module

The **MLflow Integration Module** provides a collection of tools and utilities to integrate MLflow into your machine learning workflows. It includes classes for managing experiments, tracking runs, fine-tuning models, and loading registered models. This module is intended to simplify the process of experiment tracking, model management, and deployment within an MLflow environment.

## Current Functionality

### 1. Experiment and Run Management
- **TrackingManager** (in `tracking.py`)
  - Set or create experiments.
  - Start and end MLflow runs.
  - Log metrics, parameters, and artifacts to runs.
  - Retrieve experiment details and list runs.
  
- **MLflowManager** (in `mlflow_manager.py`)
  - Create experiments (with automatic creation if an experiment does not exist).
  - Log metrics, parameters, and artifacts to a specific run.
  - Start and terminate runs using the low-level MLflow client.
  - Retrieve detailed run information (including logged artifacts).

### 2. Model Fine-Tuning and Tracking
- **ModelFineTuner** (in `model_fine_tuner.py`)
  - Load datasets from CSV files.
  - Split data into training and testing sets.
  - Fine-tune models using provided hyperparameters.
  - Evaluate models using accuracy, F1 score, and mean squared error (currently aimed at classification tasks).
  - Track models and log additional artifacts using MLflow.

### 3. Model Loading and Inference
- **ModelLoader** (in `model_loader.py`)
  - Load a model from MLflow using its URI (e.g., `models:/model_name/version`).
  - Make predictions using loaded models.
  - List all registered models.
  - Retrieve version information for a specific model.
  - Transition a model version to a different stage (e.g., from "Staging" to "Production").

## Functionality To Be Implemented (TBI)

- **Enhanced Error Handling & Logging:**
  - Improve error reporting and add additional logging for troubleshooting.
  
- **Support for Multiple Model Frameworks:**
  - Extend fine-tuning and tracking utilities to support frameworks other than scikit-learn.
  
- **Hyperparameter Optimization:**
  - Integrate hyperparameter search strategies (e.g., grid search, Bayesian optimization) and track experiments accordingly.
  
- **Distributed Training Support:**
  - Add features for tracking and managing distributed training jobs.
  
- **Improved Model Registry Integration:**
  - Enhance capabilities for managing model versions and transitions within the MLflow Model Registry.
  
- **User Interface Enhancements:**
  - Develop a front-end or dashboard for visualizing experiment and run metrics.

<!-- ## Usage Examples

### Tracking an Experiment
```python
from mlflow_integration.tracking import TrackingManager

tracking_manager = TrackingManager(tracking_uri="http://localhost:5000")
experiment_id = tracking_manager.set_experiment("My Experiment")
run_id = tracking_manager.start_run(run_name="Initial Run")
tracking_manager.log_params({"param1": "value1"})
tracking_manager.log_metrics({"accuracy": 0.95})
tracking_manager.end_run() -->
