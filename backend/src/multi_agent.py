from dotenv import load_dotenv
from core.agents.agent import Agent

def simulate_consciousness(response) -> dict:
    """
    Simulates a conversation among three agents and returns a structured dictionary.

    Parameters:
        response (Multimodal_Agent_Parameter): Object containing system prompts and user prompt.

    Returns:
        dict: A dictionary where keys are agent names and values are their responses.
    """
    # Load environment variables
    load_dotenv()

    # Instantiate agents with provided system prompts
    analytica = Agent(name="Analytica", system_prompt=response.system_prompt_analytica)
    creativa = Agent(name="Creativa", system_prompt=response.system_prompt_creativa)
    pragmatica = Agent(name="Pragmatica", system_prompt=response.system_prompt_pragmatica)

    # Store responses in a dictionary
    responses = {}

    # Agent interaction flow
    responses["Analytica"] = analytica.execute_task(response.user_prompt)
    responses["Creativa"] = creativa.execute_task(responses["Analytica"])
    responses["Pragmatica"] = pragmatica.execute_task(responses["Creativa"])
    responses["Final_Analytica"] = analytica.execute_task(responses["Pragmatica"])

    return responses
