from api_integration.default_api import log_workflow, get_workflow_summary, detect_workflow_bottlenecks
from typing import Dict, Any, List


class WorkflowHelper:
    """
    Utility class for managing workflows in the CLI.
    """

    @staticmethod
    def start_workflow(workflow_id: str, agent_name: str, initial_task: str) -> Dict[str, Any]:
        """
        Start a new workflow by logging its initial task.

        Args:
            workflow_id (str): Unique ID for the workflow.
            agent_name (str): Name of the agent responsible for the workflow.
            initial_task (str): Description of the initial task.

        Returns:
            Dict[str, Any]: Success message or error details.
        """
        try:
            log_workflow({
                "workflow_id": workflow_id,
                "agent_name": agent_name,
                "activity": initial_task,
                "status": "started"
            })
            return {"status": "success", "message": f"Workflow '{workflow_id}' started successfully."}
        except Exception as e:
            return {"status": "error", "message": f"Failed to start workflow '{workflow_id}': {e}"}

    @staticmethod
    def approve_task(workflow_id: str, agent_name: str, task_description: str) -> Dict[str, Any]:
        """
        Approve a task in a workflow by logging its status as 'approved'.

        Args:
            workflow_id (str): Unique ID for the workflow.
            agent_name (str): Name of the agent handling the task.
            task_description (str): Description of the task to approve.

        Returns:
            Dict[str, Any]: Success message or error details.
        """
        try:
            log_workflow({
                "workflow_id": workflow_id,
                "agent_name": agent_name,
                "activity": task_description,
                "status": "approved"
            })
            return {"status": "success", "message": f"Task '{task_description}' in workflow '{workflow_id}' approved successfully."}
        except Exception as e:
            return {"status": "error", "message": f"Failed to approve task '{task_description}' in workflow '{workflow_id}': {e}"}

    @staticmethod
    def generate_report(workflow_id: str) -> Dict[str, Any]:
        """
        Generate a summary report for a specific workflow.

        Args:
            workflow_id (str): Unique ID of the workflow.

        Returns:
            Dict[str, Any]: Workflow summary or error details.
        """
        try:
            summary = get_workflow_summary(workflow_id)
            return {"status": "success", "summary": summary}
        except Exception as e:
            return {"status": "error", "message": f"Failed to generate report for workflow '{workflow_id}': {e}"}

    @staticmethod
    def detect_bottlenecks(workflow_id: str, threshold_minutes: int = 10) -> Dict[str, Any]:
        """
        Detect bottlenecks in a workflow based on time thresholds.

        Args:
            workflow_id (str): Unique ID of the workflow.
            threshold_minutes (int): Time threshold for bottlenecks (in minutes).

        Returns:
            Dict[str, Any]: Bottlenecks information or error details.
        """
        try:
            bottlenecks = detect_workflow_bottlenecks(workflow_id, threshold_minutes)
            return {"status": "success", "bottlenecks": bottlenecks}
        except Exception as e:
            return {"status": "error", "message": f"Failed to detect bottlenecks for workflow '{workflow_id}': {e}"}

    @staticmethod
    def validate_workflow_id(workflow_id: str) -> bool:
        """
        Validate the format of a workflow ID.

        Args:
            workflow_id (str): Workflow ID to validate.

        Returns:
            bool: True if valid, False otherwise.
        """
        if not workflow_id or len(workflow_id) < 3:
            return False
        # Add additional validation rules as needed
        return True


# Example Usage
if __name__ == "__main__":
    # Example data
    workflow_id = "workflow1"
    agent_name = "Agent1"
    initial_task = "Prepare dataset for analysis"

    # Start a workflow
    result = WorkflowHelper.start_workflow(workflow_id, agent_name, initial_task)
    print(result)

    # Approve a task
    task_result = WorkflowHelper.approve_task(workflow_id, agent_name, "Finalize model training")
    print(task_result)

    # Generate a report
    report_result = WorkflowHelper.generate_report(workflow_id)
    print(report_result)

    # Detect bottlenecks
    bottlenecks_result = WorkflowHelper.detect_bottlenecks(workflow_id, threshold_minutes=15)
    print(bottlenecks_result)
