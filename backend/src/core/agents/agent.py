import questionary as qy
from api_agent import api_Agent

from langgraph.checkpoint.memory import MemorySaver
from langgraph.graph import START, MessagesState, StateGraph


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
    
    def call_model(self, state: MessagesState):
        response = self.agent.llm.invoke(state["messages"])
        return {"messages": response}

    
    def init_app(self):
        self.workflow = StateGraph(state_schema=MessagesState)
        self.workflow.add_edge(START, "model")
        self.workflow.add_node("model", self.call_model)  
        self.memory = MemorySaver()
        self.app = self.workflow.compile(checkpointer=self.memory)

        
    def invoke_app(self, content, config):
        output = self.app.invoke(content, config)
        
        return output
    