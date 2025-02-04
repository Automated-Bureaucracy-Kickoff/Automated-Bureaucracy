
import questionary as qy
from api_embed import api_Embed

from langchain_core.vectorstores import InMemoryVectorStore
from langgraph.checkpoint.memory import MemorySaver
from langchain_core.messages import HumanMessage, SystemMessage
from ..vars import *
from core.tools.search import search
from core.tools.pdf_loader import load_pdf, load_dir_of_pdfs
from langgraph.prebuilt import create_react_agent


class EmbedAgent():
    """
    prompts for which AI provider you want to use, from a list then
    then prompts which model from the provider
    """
    def create_agent(self):
        provider = qy.select("Which provider",
                embed_models_by_prov.keys()).ask()
        name = qy.text("Name for agent?").ask()
        agent = api_Embed(name=name, provider=provider)
        print("")
        self.model = qy.select("Which Model", 
                        embed_models_by_prov[provider]
                        ).ask() 
        agent.init_model(model=self.model)
        print("")
        self.agent = agent.agent
        return
    
    def invoke_agent(self, prompt, config=None):
        # For embeddings, you typically don't need to include system or human messages.
        # Simply compute and return the embedding for the prompt.
        output = self.agent.embed(prompt)
        return output
    