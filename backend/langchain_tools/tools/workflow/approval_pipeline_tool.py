"""
Approval Pipeline Tool
This module defines the ApprovalPipelineTool class, which automates multi-step approval workflows.
"""

from typing import List, Dict, Any


class ApprovalPipelineTool:
    """
    Automates multi-step approval workflows by managing tasks, approvals, and rejections across multiple agents.
    """

    def __init__(self):
        """
        Initialize the approval pipeline tool.
        """
        self.pipeline = []

    def add_task(self, task_name: str, approvers: List[str], task_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Add a new task to the approval pipeline.

        Args:
            task_name (str): Name of the task.
            approvers (List[str]): List of approvers for the task.
            task_data (Dict[str, Any]): Additional data associated with the task.

        Returns:
            Dict[str, Any]: The newly added task.
        """
        task = {
            "task_name": task_name,
            "approvers": approvers,
            "task_data": task_data,
            "status": "Pending",
            "approved_by": [],
            "rejected_by": []
        }
        self.pipeline.append(task)
        return task

    def approve_task(self, task_name: str, approver: str) -> str:
        """
        Approve a task in the pipeline.

        Args:
            task_name (str): Name of the task to approve.
            approver (str): Name of the approver.

        Returns:
            str: Status of the task after the approval.
        """
        for task in self.pipeline:
            if task["task_name"] == task_name:
                if approver not in task["approvers"]:
                    return f"{approver} is not authorized to approve this task."
                if approver in task["approved_by"]:
                    return f"{approver} has already approved this task."
                task["approved_by"].append(approver)
                if set(task["approved_by"]) == set(task["approvers"]):
                    task["status"] = "Approved"
                return f"Task '{task_name}' approved by {approver}."
        return f"Task '{task_name}' not found in the pipeline."

    def reject_task(self, task_name: str, approver: str) -> str:
        """
        Reject a task in the pipeline.

        Args:
            task_name (str): Name of the task to reject.
            approver (str): Name of the approver.

        Returns:
            str: Status of the task after the rejection.
        """
        for task in self.pipeline:
            if task["task_name"] == task_name:
                if approver not in task["approvers"]:
                    return f"{approver} is not authorized to reject this task."
                if approver in task["rejected_by"]:
                    return f"{approver} has already rejected this task."
                task["rejected_by"].append(approver)
                task["status"] = "Rejected"
                return f"Task '{task_name}' rejected by {approver}."
        return f"Task '{task_name}' not found in the pipeline."

    def get_task_status(self, task_name: str) -> Dict[str, Any]:
        """
        Retrieve the status of a specific task.

        Args:
            task_name (str): Name of the task.

        Returns:
            Dict[str, Any]: Task details including current status.
        """
        for task in self.pipeline:
            if task["task_name"] == task_name:
                return task
        return {"error": f"Task '{task_name}' not found in the pipeline."}

    def list_all_tasks(self) -> List[Dict[str, Any]]:
        """
        List all tasks in the pipeline.

        Returns:
            List[Dict[str, Any]]: All tasks in the pipeline.
        """
        return self.pipeline


# Example Usage
if __name__ == "__main__":
    tool = ApprovalPipelineTool()

    # Add a task
    task = tool.add_task(
        task_name="Approve Budget",
        approvers=["Alice", "Bob"],
        task_data={"budget": 5000, "description": "Quarterly budget approval"}
    )
    print("Task Added:", task)

    # Approve the task
    print(tool.approve_task("Approve Budget", "Alice"))
    print(tool.approve_task("Approve Budget", "Bob"))

    # Check task status
    print("Task Status:", tool.get_task_status("Approve Budget"))

    # Reject the task
    print(tool.reject_task("Approve Budget", "Bob"))

    # List all tasks
    print("All Tasks:", tool.list_all_tasks())
