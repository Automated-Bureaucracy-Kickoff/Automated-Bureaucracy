from api_integration.default_api import create_agent
import argparse

def start_agent(name, system_prompt, openai_api_key, tavily_api_key, mlflow_uri):
    """
    Starts a new agent using the backend API.

    Args:
        name (str): The name of the agent.
        system_prompt (str): The system prompt for the agent.
        openai_api_key (str): OpenAI API key for the agent.
        tavily_api_key (str): Tavily API key for internet access.
        mlflow_uri (str): URI for MLflow integration.
    """
    try:
        response = create_agent({
            "name": name,
            "system_prompt": system_prompt,
            "openai_api_key": openai_api_key,
            "tavily_api_key": tavily_api_key,
            "mlflow_uri": mlflow_uri,
        })
        print(f"Agent '{name}' started successfully.")
        print(f"Response: {response}")
    except Exception as e:
        print(f"Error starting agent '{name}': {e}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Start a new agent.")
    parser.add_argument("--name", required=True, help="Name of the agent.")
    parser.add_argument("--system-prompt", required=True, help="System prompt for the agent.")
    parser.add_argument("--openai-api-key", required=True, help="OpenAI API key.")
    parser.add_argument("--tavily-api-key", required=True, help="Tavily API key for internet access.")
    parser.add_argument("--mlflow-uri", required=True, help="URI for MLflow integration.")

    args = parser.parse_args()
    start_agent(
        name=args.name,
        system_prompt=args.system_prompt,
        openai_api_key=args.openai_api_key,
        tavily_api_key=args.tavily_api_key,
        mlflow_uri=args.mlflow_uri,
    )
