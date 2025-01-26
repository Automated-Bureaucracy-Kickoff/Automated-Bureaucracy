import argparse
from Agent import Agent


def create_agent(args):
    """
    Create an agent instance based on user inputs.
    """
    global agent
    agent = Agent(
        name=args.name,
        system_prompt=args.system_prompt,
        openai_api_key=args.openai_api_key,
        tavily_api_key=args.tavily_api_key,
        mlflow_uri=args.mlflow_uri,
    )
    print(f"Agent '{args.name}' created successfully!")


def execute_task(args):
    """
    Execute a task using the agent.
    """
    if not agent:
        print("No agent instance found. Create an agent first!")
        return
    result = agent.execute_task(args.task)
    print(f"Task Result: {result}")


def reflect(args):
    """
    Reflect using the agent's notepad tool.
    """
    if not agent:
        print("No agent instance found. Create an agent first!")
        return
    result = agent.reflect(args.input)
    print(f"Reflection Result: {result}")


def search_internet(args):
    """
    Perform an internet search using the agent.
    """
    if not agent:
        print("No agent instance found. Create an agent first!")
        return
    result = agent.search_internet(args.query)
    print(f"Internet Search Result: {result}")


def log_model(args):
    """
    Log a model's metadata and metrics using MLflow.
    """
    if not agent:
        print("No agent instance found. Create an agent first!")
        return
    agent.log_model(
        model_name=args.model_name,
        params={"param1": args.param1, "param2": args.param2},
        metrics={"accuracy": args.accuracy, "f1_score": args.f1_score},
    )
    print(f"Model '{args.model_name}' logged successfully!")


def setup_parser():
    """
    Set up CLI argument parser.
    """
    parser = argparse.ArgumentParser(
        description="CLI for testing the Agent class and its functionalities."
    )
    subparsers = parser.add_subparsers()

    # Create agent command
    create_parser = subparsers.add_parser("create", help="Create a new agent.")
    create_parser.add_argument("--name", required=True, help="Agent name.")
    create_parser.add_argument(
        "--system-prompt", required=True, help="System prompt for the agent."
    )
    create_parser.add_argument(
        "--openai-api-key", required=True, help="API key for OpenAI."
    )
    create_parser.add_argument(
        "--tavily-api-key", required=True, help="API key for Tavily."
    )
    create_parser.add_argument("--mlflow-uri", required=True, help="MLflow URI.")
    create_parser.set_defaults(func=create_agent)

    # Execute task command
    task_parser = subparsers.add_parser("task", help="Execute a task using the agent.")
    task_parser.add_argument("--task", required=True, help="Task prompt to execute.")
    task_parser.set_defaults(func=execute_task)

    # Reflect command
    reflect_parser = subparsers.add_parser(
        "reflect", help="Use the agent's reflection tool."
    )
    reflect_parser.add_argument("--input", required=True, help="Reflection input text.")
    reflect_parser.set_defaults(func=reflect)

    # Internet search command
    search_parser = subparsers.add_parser(
        "search", help="Perform an internet search using the agent."
    )
    search_parser.add_argument("--query", required=True, help="Search query.")
    search_parser.set_defaults(func=search_internet)

    # Log model command
    log_model_parser = subparsers.add_parser(
        "log", help="Log a model's metadata and metrics."
    )
    log_model_parser.add_argument(
        "--model-name", required=True, help="Name of the model."
    )
    log_model_parser.add_argument("--param1", required=True, help="Model parameter 1.")
    log_model_parser.add_argument("--param2", required=True, help="Model parameter 2.")
    log_model_parser.add_argument(
        "--accuracy", required=True, type=float, help="Model accuracy."
    )
    log_model_parser.add_argument(
        "--f1-score", required=True, type=float, help="Model F1 score."
    )
    log_model_parser.set_defaults(func=log_model)

    return parser


if __name__ == "__main__":
    # Parse arguments and execute corresponding function
    parser = setup_parser()
    args = parser.parse_args()

    # Initialize the agent globally
    agent = None

    # Execute the CLI function
    if hasattr(args, "func"):
        args.func(args)
    else:
        parser.print_help()
