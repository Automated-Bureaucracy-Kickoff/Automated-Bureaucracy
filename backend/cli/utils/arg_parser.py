import argparse

def get_arg_parser():
    """
    Creates and returns the argument parser for the CLI.

    Returns:
        argparse.ArgumentParser: Configured argument parser.
    """
    parser = argparse.ArgumentParser(description="Automated Bureaucracy CLI")

    subparsers = parser.add_subparsers(title="Commands", dest="command")

    # Agent-related commands
    agent_parser = subparsers.add_parser("agent", help="Agent management commands")
    agent_subparsers = agent_parser.add_subparsers(dest="agent_command")

    # Create agent
    create_agent_parser = agent_subparsers.add_parser("create", help="Create a new agent")
    create_agent_parser.add_argument("--name", required=True, help="Name of the agent")
    create_agent_parser.add_argument("--system-prompt", required=True, help="System prompt for the agent")
    create_agent_parser.add_argument("--openai-api-key", required=True, help="OpenAI API key")
    create_agent_parser.add_argument("--tavily-api-key", required=True, help="Tavily API key")
    create_agent_parser.add_argument("--mlflow-uri", required=True, help="MLflow tracking URI")

    # Stop agent
    stop_agent_parser = agent_subparsers.add_parser("stop", help="Stop a running agent")
    stop_agent_parser.add_argument("--name", required=True, help="Name of the agent to stop")

    # List agents
    agent_subparsers.add_parser("list", help="List all active agents")

    # Workflow-related commands
    workflow_parser = subparsers.add_parser("workflow", help="Workflow management commands")
    workflow_subparsers = workflow_parser.add_subparsers(dest="workflow_command")

    # Start workflow
    start_workflow_parser = workflow_subparsers.add_parser("start", help="Start a new workflow")
    start_workflow_parser.add_argument("--workflow-id", required=True, help="Unique ID for the workflow")
    start_workflow_parser.add_argument("--agent-name", required=True, help="Name of the agent managing the workflow")
    start_workflow_parser.add_argument("--initial-task", required=True, help="Description of the initial task")

    # Approve task
    approve_task_parser = workflow_subparsers.add_parser("approve", help="Approve a task in a workflow")
    approve_task_parser.add_argument("--workflow-id", required=True, help="Unique ID for the workflow")
    approve_task_parser.add_argument("--agent-name", required=True, help="Name of the agent handling the task")
    approve_task_parser.add_argument("--task-description", required=True, help="Description of the task to approve")

    # Generate report
    generate_report_parser = workflow_subparsers.add_parser("report", help="Generate a workflow report")
    generate_report_parser.add_argument("--workflow-id", required=True, help="Unique ID of the workflow")

    return parser
