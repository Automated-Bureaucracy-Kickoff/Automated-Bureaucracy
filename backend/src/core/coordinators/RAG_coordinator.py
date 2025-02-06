from ..agents.chat.chat_agent import ChatAgent
from ..agents.embed.embed_agent import EmbedAgent
from langgraph.graph import START, StateGraph, END
from langchain_text_splitters import RecursiveCharacterTextSplitter
from .state import State

class coordinator():
    
    def __init__(self):
        self.graph_builder = StateGraph(State)
        self.text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
        self.vector_store = 
        
    def add_chat_agent(self, agent: ChatAgent):
        self.chat_agent = agent
    
    def add_embed_agent(self, agent: EmbedAgent):
        self.embed_agent = agent

    def init_graph(self):        
            
        
        
    
        