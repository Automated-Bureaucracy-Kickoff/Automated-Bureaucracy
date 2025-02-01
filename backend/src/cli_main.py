import questionary as qy
from core.agents.api_agent import api_Agent


def get_agent() -> api_Agent:
    name = qy.text("What is your agents name").ask()
    print("")
    provider = qy.select("Which provider",
              choices = ["openai","google"]).ask()
    agent = api_Agent(name=name, provider=provider)
    print("")
    model = qy.select("Which Model", 
                      choices = agent.get_provider_model_names()
                      ).ask() 
    agent.init_model(model=model)
    print("")
    return agent
    
    
def chat(agent: api_Agent, message: str) -> str:
    response =  agent.llm.invoke(message)
    return response


def main():
    print("Welcome to Automated Bureaucracy via Command Line")
    print("")
    choice = qy.select( "What do you want to do",
              choices=[
                  "Chat","Exit"
                  ]
    ).ask()
    
    if choice == "Chat":
        agent = get_agent()
        print("")
        message = ""
        while message != "exit":
            message = qy.text("what is your prompt or exit to leave").ask()
            response = chat(agent, message)
            print(response.content)
        print("")
    
    else:
        exit()
    

if __name__ == "__main__":
    main()
