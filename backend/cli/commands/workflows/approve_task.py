from api_integration.default_api import log_workflow
import argparse


def approve_task(workflow_id, agent_name, task_description):
    """
    Approve a task in the workflow by logging its status as 'approved'.

    Args:
        workflow_id (str): Unique ID of the workflow.
        agent_name (str): Name of the agent handling the task.
        task_description (str): Description of the task to approve.
    """
    try:
        log_workflow({
            "workflow_id": workflow_id,
            "agent_name": agent_name,
            "activity": task_description,
            "status": "approved"
        })
        print(f"Task '{task_description}' in workflow '{workflow_id}' approved successfully.")
    except Exception as e:
        print(f"Error approving task '{task_description}' in workflow '{workflow_id}': {e}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Approve a task in a workflow.")
    parser.add_argument("--workflow-id", required=True, help="The unique ID of the workflow.")
    parser.add_argument("--agent-name", required=True, help="The name of the agent handling the task.")
    parser.add_argument("--task-description", required=True, help="Description of the task to approve.")

    args = parser.parse_args()
    approve_task(
        workflow_id=args.workflow_id,
        agent_name=args.agent_name,
        task_description=args.task_description,
    )
