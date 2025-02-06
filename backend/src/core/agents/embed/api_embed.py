from langchain_openai import OpenAIEmbeddings
from openai import OpenAI
import google.generativeai as genai
from langchain_google_genai import GoogleGenerativeAIEmbeddings


class api_Embed():
    def __init__(self, name, provider):
        self.provider = provider
        self.name = name
        
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
            # Filter for models whose IDs contain 'embedding'
            return [model.id for model in models.data if "embedding" in model.id]
        elif self.provider == "google":
            genai.configure(api_key=self.apikey)
            models = genai.list_models()
            # Filter based on name, assuming embedding models include 'embedding' (adjust if needed)
            return [model.name.split('/')[-1] for model in models if "embedding" in model.name.lower()]
        
    
    def init_model(self, model):
        if model in self.get_provider_model_names():
            self.model_name = model
        else:
            print(f"invalid model name for {self.provider}")
        
        if self.provider == "openai":
            self.agent = OpenAIEmbeddings(model=self.model_name)
        
        elif self.provider == "google":
            self.agent = GoogleGenerativeAIEmbeddings(model=self.model_name)
            
            
                

        


    