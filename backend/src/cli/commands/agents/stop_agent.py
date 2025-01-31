from api_integration.default_api import stop_agent
import argparse

def stop_agent_by_name(agent_name):
    """
    Stops a running agent via the backend API.

    Args:
        agent_name (str): The name of the agent to stop.
    """
    try:
        response = stop_agent({"name": agent_name})
        print(f"Agent '{agent_name}' stopped successfully.")
        print(f"Response: {response}")
    except Exception as e:
        print(f"Error stopping agent '{agent_name}': {e}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Stop a running agent.")
    parser.add_argument("--name", required=True, help="Name of the agent to stop.")

    args = parser.parse_args()
    stop_agent_by_name(agent_name=args.name)
