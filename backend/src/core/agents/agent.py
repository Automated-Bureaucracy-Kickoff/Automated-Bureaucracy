import questionary as qy
from api_agent import api_Agent
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