import os
from langchain_openai import ChatOpenAI
from openai import OpenAI
from langchain_google_genai import ChatGoogleGenerativeAI
import google.generativeai as genai
from langgraph.checkpoint.memory import MemorySaver
from langgraph.graph import START, MessagesState, StateGraph


class api_Agent():
    def __init__(self, name, provider):
        self.name = name
        self.provider = provider
        
        if self.provider == "openai":
            from env import openai_api_key
            self.apikey = openai_api_key
        elif self.provider == "google":
            from env import google_api_key
            self.apikey  = google_api_key
        else:
            print("Invalid Provider")
            
    def get_provider_model_names(self):
        if self.provider == "openai":
            client = OpenAI(api_key=self.apikey)
            models = client.models.list()
            # Extract and return the list of model IDs
            return [model.id for model in models.data]
        elif self.provider == "google":
            genai.configure(api_key=self.apikey)
            models = genai.list_models()
            # Assuming genai.list_models() returns a generator of model objects
            return [model.name.split('/')[-1] for model in models]
        
    
    def init_model(self, model):
        if model in self.get_provider_model_names():
            self.model_name = model
        else:
            print(f"invalid model name for {self.provider}")
            
        if self.model_name:
            print("HI")
            
            if self.provider == "openai":
                self.llm = ChatOpenAI(model=self.model_name, api_key=self.apikey)
            elif self.provider == "google":
                print("HI")
                self.llm = ChatGoogleGenerativeAI(model=self.model_name, api_key=self.apikey)
                

        
    