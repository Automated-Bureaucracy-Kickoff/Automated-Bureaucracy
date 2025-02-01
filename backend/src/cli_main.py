import questionary as qy
from core.agents.api_agent import api_Agent


class Agent():

    def create_agent(self):
        self.name = qy.text("What is your agents name").ask()
        print("")
        provider = qy.select("Which provider",
                choices = ["openai","google"]).ask()
        agent = api_Agent(name=self.name, provider=provider)
        print("")
        self.model = qy.select("Which Model", 
                        choices = agent.get_provider_model_names()
                        ).ask() 
        agent.init_model(model=self.model)
        print("")
        self.agent = agent
        return
    def chat(self,message: str) -> str:
        response =  self.agent.llm.invoke(message)
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
        agent = Agent()
        agent.create_agent()
        print("")
        message = ""
        while message != "Exit":
            message = qy.text("what is your prompt or exit to leave").ask()
            response = agent.chat(message)
            print(response.content)
        print("")
    
    else:
        exit()
    

if __name__ == "__main__":
    main()
    print("hello")
