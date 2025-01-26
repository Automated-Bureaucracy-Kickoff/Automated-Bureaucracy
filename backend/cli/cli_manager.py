import argparse
from api_integration.default_api import (
    create_agent,
    list_agents,
    execute_task,
    log_workflow,
    get_workflow_summary,
    detect_workflow_bottlenecks,
    generate_compliance_report,
)

def handle_create_agent(args):
    """
    Handles the creation of an agent via the CLI.
    """
    agent_data = {
        "name": args.name,
        "system_prompt": args.system_prompt,
        "openai_api_key": args.openai_api_key,
        "tavily_api_key": args.tavily_api_key,
        "mlflow_uri": args.mlflow_uri,
    }
    response = create_agent(agent_data)
    print(response)


def handle_list_agents(args):
    """
    Handles listing of agents via the CLI.
    """
    response = list_agents()
    print("Agents:", response)


def handle_execute_task(args):
    """
    Handles task execution for an agent via the CLI.
    """
    task_data = {
        "agent_name": args.agent_name,
        "task_prompt": args.task_prompt,
    }
    response = execute_task(task_data)
    print(response)


def handle_log_workflow(args):
    """
    Logs an activity for a workflow via the CLI.
    """
    workflow_data = {
        "workflow_id": args.workflow_id,
        "agent_name": args.agent_name,
        "activity": args.activity,
        "status": args.status,
    }
    response = log_workflow(workflow_data)
    print(response)


def handle_get_workflow_summary(args):
    """
    Retrieves a workflow summary via the CLI.
    """
    response = get_workflow_summary(args.workflow_id)
    print("Workflow Summary:", response)


def handle_detect_bottlenecks(args):
    """
    Detects bottlenecks in a workflow via the CLI.
    """
    response = detect_workflow_bottlenecks(args.workflow_id, args.threshold_minutes)
    print("Bottlenecks:", response)


def handle_generate_compliance_report(args):
    """
    Generates a compliance report via the CLI.
    """
    compliance_rules = [{"type": t, "value": v} for t, v in zip(args.rule_types, args.rule_values)]
    agent_logs = {
        args.agent_name: [{"timestamp": ts, "activity": act} for ts, act in zip(args.timestamps, args.activities)]
    }
    response = generate_compliance_report(agent_logs, compliance_rules)
    print(response)


def main():
    parser = argparse.ArgumentParser(description="CLI for Automated Bureaucracy Backend")
    subparsers = parser.add_subparsers()

    # Create Agent
    create_parser = subparsers.add_parser("create-agent", help="Create a new agent")
    create_parser.add_argument("--name", required=True, help="Agent name")
    create_parser.add_argument("--system-prompt", required=True, help="System prompt for the agent")
    create_parser.add_argument("--openai-api-key", required=True, help="OpenAI API key")
    create_parser.add_argument("--tavily-api-key", required=True, help="Tavily API key")
    create_parser.add_argument("--mlflow-uri", required=True, help="MLflow URI")
    create_parser.set_defaults(func=handle_create_agent)

    # List Agents
    list_parser = subparsers.add_parser("list-agents", help="List all active agents")
    list_parser.set_defaults(func=handle_list_agents)

    # Execute Task
    task_parser = subparsers.add_parser("execute-task", help="Execute a task with an agent")
    task_parser.add_argument("--agent-name", required=True, help="Agent name")
    task_parser.add_argument("--task-prompt", required=True, help="Task prompt to execute")
    task_parser.set_defaults(func=handle_execute_task)

    # Log Workflow
    log_parser = subparsers.add_parser("log-workflow", help="Log an activity for a workflow")
    log_parser.add_argument("--workflow-id", required=True, help="Workflow ID")
    log_parser.add_argument("--agent-name", required=True, help="Agent name")
    log_parser.add_argument("--activity", required=True, help="Activity description")
    log_parser.add_argument("--status", required=True, help="Activity status (e.g., in_progress, completed, failed)")
    log_parser.set_defaults(func=handle_log_workflow)

    # Workflow Summary
    summary_parser = subparsers.add_parser("workflow-summary", help="Get workflow summary")
    summary_parser.add_argument("--workflow-id", required=True, help="Workflow ID")
    summary_parser.set_defaults(func=handle_get_workflow_summary)

    # Detect Bottlenecks
    bottleneck_parser = subparsers.add_parser("detect-bottlenecks", help="Detect bottlenecks in a workflow")
    bottleneck_parser.add_argument("--workflow-id", required=True, help="Workflow ID")
    bottleneck_parser.add_argument("--threshold-minutes", type=int, default=10, help="Threshold for bottleneck detection")
    bottleneck_parser.set_defaults(func=handle_detect_bottlenecks)

    # Generate Compliance Report
    compliance_parser = subparsers.add_parser("compliance-report", help="Generate compliance report")
    compliance_parser.add_argument("--agent-name", required=True, help="Agent name")
    compliance_parser.add_argument("--timestamps", nargs="+", required=True, help="Timestamps of activities")
    compliance_parser.add_argument("--activities", nargs="+", required=True, help="Descriptions of activities")
    compliance_parser.add_argument("--rule-types", nargs="+", required=True, help="Compliance rule types")
    compliance_parser.add_argument("--rule-values", nargs="+", required=True, help="Compliance rule values")
    compliance_parser.set_defaults(func=handle_generate_compliance_report)

    # Parse arguments and execute
    args = parser.parse_args()
    if hasattr(args, "func"):
        args.func(args)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
