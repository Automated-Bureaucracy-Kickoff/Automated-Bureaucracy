from api_integration.default_api import log_workflow
import argparse


def start_workflow(workflow_id, agent_name, initial_task):
    """
    Start a new workflow by logging its initial task.

    Args:
        workflow_id (str): Unique ID for the workflow.
        agent_name (str): Name of the agent responsible for the workflow.
        initial_task (str): Description of the initial task.
    """
    try:
        log_workflow({
            "workflow_id": workflow_id,
            "agent_name": agent_name,
            "activity": initial_task,
            "status": "started"
        })
        print(f"Workflow '{workflow_id}' started successfully with initial task '{initial_task}'.")
    except Exception as e:
        print(f"Error starting workflow '{workflow_id}': {e}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Start a new workflow.")
    parser.add_argument("--workflow-id", required=True, help="The unique ID for the workflow.")
    parser.add_argument("--agent-name", required=True, help="The name of the agent responsible for the workflow.")
    parser.add_argument("--initial-task", required=True, help="The description of the initial task.")

    args = parser.parse_args()
    start_workflow(
        workflow_id=args.workflow_id,
        agent_name=args.agent_name,
        initial_task=args.initial_task,
    )
