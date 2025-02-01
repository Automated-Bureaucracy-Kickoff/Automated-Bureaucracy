import questionary as qy
from core.agents.agent import Agent
from dotenv import load_dotenv

load_dotenv()

def setup_thought_sim() -> tuple[Agent,int]:
    choice = qy.text("How many agents would you like").ask()
    print("")
    print(choice)
    print(type(choice))
    agents = []
    for i in range(int(choice)):
        name = qy.text(f"Name of agent{i}?").ask()
        print("")
        prompt = qy.text(f"Prompt for agent{i}?").ask()
        agents.append(Agent(name=name,system_prompt=prompt))
        print("")
        
    iterations = qy.text("How many iterations would you like to simulate").ask()
        
    return agents, iterations
    
def run_thought_sim(agents: list[Agent], iterations: int):
    
    response = qy.text("What is the prompt for the group of agents").ask()
    convo_segments= []
    for i in range(int(iterations)):
        for agent in agents:
            response = agent.execute_task(response)
            convo_segments.append(response)
            

    

def main():
    print("Welcome to Automated Bureaucracy via Command Line")
    print("")
    choice = qy.select( "What do you want to do",
              choices=[
                  "Run Thought Simulation","Exit"
                  ]
    ).ask()
    
    if choice == "Run Thought Simulation":
        agents,iter = setup_thought_sim()
        print("")
        run_thought_sim(agents,iter)
        print("")
    
    else:
        exit()
        
    

if __name__ == "__main__":
    main()
