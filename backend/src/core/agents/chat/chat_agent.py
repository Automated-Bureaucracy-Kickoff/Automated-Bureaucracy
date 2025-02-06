import questionary as qy
from ..api_agent import api_Agent

from langchain_core.vectorstores import InMemoryVectorStore
from langgraph.checkpoint.memory import MemorySaver
from langchain_core.messages import HumanMessage, SystemMessage
from ..vars import *
from core.tools.search import search
from core.tools.pdf_loader import load_pdf, load_dir_of_pdfs
from langgraph.prebuilt import create_react_agent


class ChatAgent():
    """
    prompts for which AI provider you want to use, from a list then
    then prompts which model from the provider
    """
    def create_agent(self):
        provider = qy.select("Which provider",
                chat_models_by_prov.keys()).ask()
        name = qy.text("Name for agent?").ask()
        agent = api_Agent(name=name, provider=provider)
        print("")
        self.model = qy.select("Which Model", 
                        chat_models_by_prov[provider]
                        ).ask() 
        agent.init_model(model=self.model)
        print("")
        self.memory = MemorySaver()
        tools = [search, load_pdf, load_dir_of_pdfs]
        agent = create_react_agent(agent.llm, tools ,checkpointer=self.memory)
        self.agent = agent
        return
    
    def set_system_message(self, message):
        self.set_system_message = message
    
    def invoke_agent(self, prompt, config):
        if self.system_prompt:
            
            content = [
                SystemMessage(
                    content=self.system_message
                ),
                HumanMessage(
                    content=prompt
                )
            ]
        else:
            content = [
                HumanMessage(
                    content=prompt
                )
            ]
        output = self.agent.invoke(content, config)
        
        return output
    