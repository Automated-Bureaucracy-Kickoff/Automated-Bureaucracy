from api_integration.default_api import list_agents

def list_all_agents():
    """
    Fetches and displays the list of active agents.
    """
    try:
        agents = list_agents()
        if not agents.get("agents"):
            print("No active agents found.")
        else:
            print("Active Agents:")
            for agent in agents["agents"]:
                print(f"- {agent}")
    except Exception as e:
        print(f"Error retrieving agents: {e}")


if __name__ == "__main__":
    list_all_agents()
