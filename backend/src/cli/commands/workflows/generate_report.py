from api_integration.default_api import get_workflow_summary
import argparse


def generate_report(workflow_id):
    """
    Generate a summary report for a specific workflow.

    Args:
        workflow_id (str): Unique ID of the workflow.
    """
    try:
        report = get_workflow_summary(workflow_id)
        print(f"Workflow Report for '{workflow_id}':")
        print("====================================")
        for key, value in report.items():
            print(f"{key}: {value}")
    except Exception as e:
        print(f"Error generating report for workflow '{workflow_id}': {e}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate a workflow report.")
    parser.add_argument("--workflow-id", required=True, help="The unique ID of the workflow.")

    args = parser.parse_args()
    generate_report(workflow_id=args.workflow_id)
