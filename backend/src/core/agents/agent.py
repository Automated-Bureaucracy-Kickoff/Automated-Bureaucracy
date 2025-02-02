import questionary as qy
from .api_agent import api_Agent

from langgraph.checkpoint.memory import MemorySaver
from langchain_core.messages import HumanMessage
from langgraph.graph import START, MessagesState
from .vars import *
from core.tools.search import search
from langgraph.prebuilt import create_react_agent

class Agent():
    """
    prompts for which AI provider you want to use, from a list then
    then prompts which model from the provider
    """
    def create_agent(self):
        provider = qy.select("Which provider",
                models_by_prov.keys()).ask()
        agent = api_Agent(provider=provider)
        print("")
        self.model = qy.select("Which Model", 
                        models_by_prov[provider]
                        ).ask() 
        agent.init_model(model=self.model)
        print("")
        self.memory = MemorySaver()
        agent = create_react_agent(agent.llm, [search],checkpointer=self.memory)
        self.agent = agent
        return
    
    """
    prompts the ai model with a message and returns a dict containing its response
    """

    
    def invoke_agent(self, content, config):
        output = self.agent.invoke({"messages":[HumanMessage(content)]}, config)
        
        return output
    