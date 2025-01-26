import matplotlib.pyplot as plt
import seaborn as sns
from typing import List, Dict, Any


class DataVisualizer:
    """
    A utility class for visualizing simulation results, including ensemble and singleton simulations.
    """

    def __init__(self):
        sns.set_theme(style="whitegrid")

    def visualize_singleton_simulation(self, data: List[Dict[str, Any]], metric: str):
        """
        Visualizes results for a singleton simulation.

        Args:
            data (List[Dict[str, Any]]): A list of dictionaries containing simulation results.
            metric (str): The metric to visualize (e.g., "task_duration", "accuracy").
        """
        values = [entry[metric] for entry in data if metric in entry]
        timestamps = [entry["timestamp"] for entry in data if "timestamp" in entry]

        plt.figure(figsize=(10, 6))
        sns.lineplot(x=timestamps, y=values, marker="o")
        plt.title(f"Singleton Simulation Analysis ({metric})", fontsize=14)
        plt.xlabel("Timestamp", fontsize=12)
        plt.ylabel(metric.capitalize(), fontsize=12)
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

    def visualize_ensemble_simulation(self, ensemble_data: List[Dict[str, Any]], metric: str):
        """
        Visualizes results for an ensemble simulation.

        Args:
            ensemble_data (List[Dict[str, Any]]): A list of dictionaries, each containing aggregated simulation results.
            metric (str): The metric to visualize (e.g., "mean_accuracy", "max_response_time").
        """
        simulation_names = [entry["name"] for entry in ensemble_data if "name" in entry]
        values = [entry[metric] for entry in ensemble_data if metric in entry]

        plt.figure(figsize=(12, 6))
        sns.barplot(x=simulation_names, y=values, palette="Blues_d")
        plt.title(f"Ensemble Simulation Analysis ({metric})", fontsize=14)
        plt.xlabel("Simulation Name", fontsize=12)
        plt.ylabel(metric.capitalize(), fontsize=12)
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

    def compare_metrics(self, data: List[Dict[str, Any]], metrics: List[str]):
        """
        Compares multiple metrics across a dataset.

        Args:
            data (List[Dict[str, Any]]): A list of dictionaries containing simulation data.
            metrics (List[str]): List of metrics to compare (e.g., ["accuracy", "response_time"]).
        """
        metric_data = {metric: [entry.get(metric, None) for entry in data] for metric in metrics}
        timestamps = [entry["timestamp"] for entry in data if "timestamp" in entry]

        plt.figure(figsize=(12, 6))
        for metric, values in metric_data.items():
            sns.lineplot(x=timestamps, y=values, label=metric, marker="o")

        plt.title("Metric Comparison Across Simulations", fontsize=14)
        plt.xlabel("Timestamp", fontsize=12)
        plt.ylabel("Values", fontsize=12)
        plt.legend(title="Metrics")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

    def heatmap_analysis(self, matrix: List[List[float]], labels: List[str]):
        """
        Displays a heatmap for matrix-style data.

        Args:
            matrix (List[List[float]]): 2D list representing matrix data.
            labels (List[str]): List of labels for rows/columns.
        """
        plt.figure(figsize=(8, 6))
        sns.heatmap(matrix, annot=True, fmt=".2f", xticklabels=labels, yticklabels=labels, cmap="coolwarm")
        plt.title("Heatmap Analysis", fontsize=14)
        plt.xlabel("Columns", fontsize=12)
        plt.ylabel("Rows", fontsize=12)
        plt.tight_layout()
        plt.show()
