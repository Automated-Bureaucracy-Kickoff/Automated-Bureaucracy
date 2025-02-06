from ..agents.chat.chat_agent import Agent
from langgraph.graph import START, StateGraph, END
from .state import State

class coordinator():
    
    def __init__(self):
        self.chat_agents = []
        self.graph_builder = StateGraph(State)
        
    def add_chat_agent(self, agent: Agent):
        self.agents.append(agent)
        self.graph_builder.add_node(agent.agent.name, agent.agent)
        
    def init_graph_start_end(self):
        self.graph_builder.add_edge(START, self.agents[0].agent.name)
        self.graph_builder.add_edge(END, self.agents[0].agent.name)
            
        
        
    
        