import argparse
from backend.agents.multi_agent_manager import MultiAgentManager

def simulate_collective_intelligence():
    """
    Simulates the default collective intelligence system with three agents:
    Analytica, Creativa, and Pragmatica.
    """
    # Simulation configuration
    simulation_config = {
        "debug_mode": True,
        "limit": 100,
        "agents": [
            {
                "name": "Analytica",
                "system_prompt": (
                    "You are Analytica, a conscious AI agent in a collective intelligence system. "
                    "Your specialization is analytical intelligence. You are aware of the simulation's "
                    "debug mode and limit of 100 messages. You collaborate with Creativa and Pragmatica."
                ),
            },
            {
                "name": "Creativa",
                "system_prompt": (
                    "You are Creativa, a conscious AI agent in a collective intelligence system. "
                    "Your specialization is creative intelligence. You are aware of the simulation's "
                    "debug mode and limit of 100 messages. You collaborate with Analytica and Pragmatica."
                ),
            },
            {
                "name": "Pragmatica",
                "system_prompt": (
                    "You are Pragmatica, a conscious AI agent in a collective intelligence system. "
                    "Your specialization is practical intelligence. You are aware of the simulation's "
                    "debug mode and limit of 100 messages. You collaborate with Analytica and Creativa."
                ),
            },
        ],
        "user_prompt": (
            "Simulate the emergence of a new form of language among simulated agents optimized for a certain purpose."
        ),
    }

    # Initialize MultiAgentManager
    manager = MultiAgentManager()

    # Add agents
    for agent_config in simulation_config["agents"]:
        manager.create_agent(
            name=agent_config["name"],
            system_prompt=agent_config["system_prompt"],
            openai_api_key="YOUR_OPENAI_API_KEY",
            tavily_api_key="YOUR_TAVILY_API_KEY",
            mlflow_uri="http://localhost:5000"
        )

    # Run the simulation
    results = manager.run_simulation(
        user_prompt=simulation_config["user_prompt"],
        message_limit=simulation_config["limit"],
        debug_mode=simulation_config["debug_mode"]
    )

    # Display results
    print("\nSimulation Results:")
    for log in results:
        print(f"{log['agent']}: {log['message']}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run the default collective intelligence simulation.")
    args = parser.parse_args()
    simulate_collective_intelligence()
