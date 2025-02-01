import numpy as np
from typing import List, Dict, Any
from sklearn.ensemble import IsolationForest
from datetime import datetime

class AnomalyDetection:
    """
    A utility class for detecting anomalies in agent behavior and system metrics.
    """

    def __init__(self):
        self.anomaly_model = IsolationForest(n_estimators=100, contamination=0.1, random_state=42)

    def fit_model(self, data: List[Dict[str, Any]], feature_key: str):
        """
        Fits the anomaly detection model using provided data.

        Args:
            data (List[Dict[str, Any]]): Input data with features to analyze.
            feature_key (str): The key to extract numeric features from the data.
        """
        features = np.array([item[feature_key] for item in data if feature_key in item]).reshape(-1, 1)
        self.anomaly_model.fit(features)
        print(f"Anomaly detection model trained on {len(features)} data points.")

    def detect_anomalies(self, data: List[Dict[str, Any]], feature_key: str) -> List[Dict[str, Any]]:
        """
        Detects anomalies in the provided data.

        Args:
            data (List[Dict[str, Any]]): Input data to analyze.
            feature_key (str): The key to extract numeric features from the data.

        Returns:
            List[Dict[str, Any]]: Data points flagged as anomalies.
        """
        features = np.array([item[feature_key] for item in data if feature_key in item]).reshape(-1, 1)
        predictions = self.anomaly_model.predict(features)
        anomalies = [data[i] for i in range(len(data)) if predictions[i] == -1]
        return anomalies

    @staticmethod
    def time_based_anomaly_detection(logs: List[Dict[str, Any]], threshold_seconds: int = 600) -> List[Dict[str, Any]]:
        """
        Identifies time-based anomalies where the gap between consecutive logs exceeds a threshold.

        Args:
            logs (List[Dict[str, Any]]): Log entries with timestamps.
            threshold_seconds (int): Time gap threshold in seconds (default: 10 minutes).

        Returns:
            List[Dict[str, Any]]: Anomalous logs with excessive time gaps.
        """
        anomalies = []
        timestamps = [datetime.fromisoformat(log["timestamp"]) for log in logs]
        for i in range(1, len(timestamps)):
            time_diff = (timestamps[i] - timestamps[i - 1]).total_seconds()
            if time_diff > threshold_seconds:
                anomalies.append({"timestamp": logs[i]["timestamp"], "gap_seconds": time_diff})
        return anomalies

    def monitor_metrics(self, metrics: List[Dict[str, Any]], metric_key: str, threshold: float) -> List[Dict[str, Any]]:
        """
        Monitors metrics for threshold-based anomalies.

        Args:
            metrics (List[Dict[str, Any]]): Metric entries with values.
            metric_key (str): The key to extract metric values from the data.
            threshold (float): The threshold for detecting anomalies.

        Returns:
            List[Dict[str, Any]]: Metrics that exceed the threshold.
        """
        anomalies = [metric for metric in metrics if metric.get(metric_key, 0) > threshold]
        return anomalies
