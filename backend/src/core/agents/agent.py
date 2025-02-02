import questionary as qy
from .api_agent import api_Agent

from langgraph.checkpoint.memory import MemorySaver
from langchain_core.messages import HumanMessage
from langgraph.graph import START, MessagesState, StateGraph
from .vars import *


class Agent():
    """
    prompts for which AI provider you want to use, from a list then
    then prompts which model from the provider
    """
    def create_agent(self):
        provider = qy.select("Which provider",
                models_by_prov.keys()).ask()
        agent = api_Agent(name=self.name, provider=provider)
        print("")
        self.model = qy.select("Which Model", 
                        models_by_prov[provider]
                        ).ask() 
        agent.init_model(model=self.model)
        print("")
        self.agent = agent
        return
    
    """
    prompts the ai model with a message and returns a dict containing its response
    """
    
    def call_model(self, state: MessagesState):
        response = self.agent.llm.invoke(state["messages"])
        return {"messages": response}

    """
    
    """
    
    def init_app(self):
        self.workflow = StateGraph(state_schema=MessagesState)
        self.workflow.add_edge(START, "model")
        self.workflow.add_node("model", self.call_model)  
        self.memory = MemorySaver()
        self.app = self.workflow.compile(checkpointer=self.memory)

        
    def invoke_app(self, content, config):
        output = self.app.invoke({"messages":[HumanMessage(content)]}, config)
        
        return output
    