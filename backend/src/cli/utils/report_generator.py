import json
import csv
from datetime import datetime
from typing import List, Dict, Any


class ReportGenerator:
    """
    Utility class for generating and exporting reports.
    """

    def __init__(self, output_dir="reports"):
        """
        Initialize the ReportGenerator.

        Args:
            output_dir (str): Directory where reports will be saved.
        """
        self.output_dir = output_dir

    def generate_report(self, data: List[Dict[str, Any]], report_name: str, file_format: str = "json") -> str:
        """
        Generate and save a report in the specified format.

        Args:
            data (List[Dict[str, Any]]): The data to include in the report.
            report_name (str): Name of the report file (without extension).
            file_format (str): Format to save the report (e.g., "json", "csv").

        Returns:
            str: Path to the generated report file.
        """
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        file_name = f"{report_name}_{timestamp}.{file_format}"
        file_path = f"{self.output_dir}/{file_name}"

        # Ensure output directory exists
        os.makedirs(self.output_dir, exist_ok=True)

        if file_format.lower() == "json":
            self._save_as_json(data, file_path)
        elif file_format.lower() == "csv":
            self._save_as_csv(data, file_path)
        else:
            raise ValueError(f"Unsupported file format: {file_format}")

        return file_path

    def _save_as_json(self, data: List[Dict[str, Any]], file_path: str):
        """
        Save data as a JSON file.

        Args:
            data (List[Dict[str, Any]]): Data to save.
            file_path (str): Path to the JSON file.
        """
        with open(file_path, "w", encoding="utf-8") as json_file:
            json.dump(data, json_file, indent=4)
        print(f"Report saved as JSON at {file_path}")

    def _save_as_csv(self, data: List[Dict[str, Any]], file_path: str):
        """
        Save data as a CSV file.

        Args:
            data (List[Dict[str, Any]]): Data to save.
            file_path (str): Path to the CSV file.
        """
        if not data:
            raise ValueError("Data is empty. Cannot save as CSV.")

        keys = data[0].keys()
        with open(file_path, "w", newline="", encoding="utf-8") as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=keys)
            writer.writeheader()
            writer.writerows(data)
        print(f"Report saved as CSV at {file_path}")


# Example Usage
if __name__ == "__main__":
    # Example data
    report_data = [
        {"id": 1, "name": "Task A", "status": "Completed", "duration": "10m"},
        {"id": 2, "name": "Task B", "status": "In Progress", "duration": "15m"},
    ]

    generator = ReportGenerator(output_dir="reports")
    json_report = generator.generate_report(report_data, report_name="workflow_report", file_format="json")
    print(f"Generated JSON report: {json_report}")

    csv_report = generator.generate_report(report_data, report_name="workflow_report", file_format="csv")
    print(f"Generated CSV report: {csv_report}")
