from datetime import datetime, timedelta
from typing import List, Dict, Any


class WorkflowMonitor:
    """
    Tracks and monitors workflows in the multi-agent system to ensure smooth operations.
    """

    def __init__(self):
        self.workflow_logs: Dict[str, List[Dict[str, Any]]] = {}

    def log_workflow_activity(self, workflow_id: str, agent_name: str, activity: str, status: str):
        """
        Logs an activity for a specific workflow.

        Args:
            workflow_id (str): The unique identifier of the workflow.
            agent_name (str): The name of the agent involved in the workflow.
            activity (str): Description of the activity.
            status (str): Status of the activity (e.g., "in_progress", "completed", "failed").
        """
        timestamp = datetime.now().isoformat()
        if workflow_id not in self.workflow_logs:
            self.workflow_logs[workflow_id] = []

        self.workflow_logs[workflow_id].append({
            "timestamp": timestamp,
            "agent_name": agent_name,
            "activity": activity,
            "status": status,
        })
        print(f"Workflow {workflow_id}: Logged activity for {agent_name} - {activity} ({status}).")

    def get_workflow_summary(self, workflow_id: str) -> Dict[str, Any]:
        """
        Provides a summary of the workflow.

        Args:
            workflow_id (str): The unique identifier of the workflow.

        Returns:
            Dict[str, Any]: A summary of the workflow, including status and activity breakdown.
        """
        if workflow_id not in self.workflow_logs:
            return {"error": f"Workflow {workflow_id} not found."}

        logs = self.workflow_logs[workflow_id]
        summary = {
            "workflow_id": workflow_id,
            "total_activities": len(logs),
            "completed": len([log for log in logs if log["status"] == "completed"]),
            "in_progress": len([log for log in logs if log["status"] == "in_progress"]),
            "failed": len([log for log in logs if log["status"] == "failed"]),
            "last_activity": logs[-1] if logs else None,
        }
        return summary

    def detect_bottlenecks(self, workflow_id: str, time_threshold_minutes: int = 10) -> List[Dict[str, Any]]:
        """
        Detects bottlenecks in the workflow by identifying long gaps between activities.

        Args:
            workflow_id (str): The unique identifier of the workflow.
            time_threshold_minutes (int): Threshold for identifying a bottleneck in minutes.

        Returns:
            List[Dict[str, Any]]: Bottleneck activities with excessive time gaps.
        """
        if workflow_id not in self.workflow_logs:
            return []

        logs = self.workflow_logs[workflow_id]
        bottlenecks = []
        timestamps = [datetime.fromisoformat(log["timestamp"]) for log in logs]

        for i in range(1, len(timestamps)):
            time_diff = (timestamps[i] - timestamps[i - 1]).total_seconds() / 60
            if time_diff > time_threshold_minutes:
                bottlenecks.append({
                    "workflow_id": workflow_id,
                    "activity": logs[i]["activity"],
                    "agent_name": logs[i]["agent_name"],
                    "time_gap_minutes": time_diff,
                })

        return bottlenecks

    def list_workflows(self) -> List[str]:
        """
        Lists all tracked workflows.

        Returns:
            List[str]: List of workflow IDs.
        """
        return list(self.workflow_logs.keys())
