import logging
from langchain.chains import SequentialChain
from langchain.prompts import PromptTemplate
from langchain.agents import Tool, initialize_agent
from tavily import TavilyClient
import mlflow
from .agent_state_manager import AgentStateManager

class Agent:
    """
    Represents an intelligent agent with OpenAI, LangChain, Tavily integration, and MLflow tracking.
    """

    def __init__(self, name, system_prompt, openai_api_key, tavily_api_key, mlflow_uri):
        logging.debug(f"Initializing agent: {name}")
        self.name = name
        self.state_manager = AgentStateManager()
        self.system_prompt = system_prompt
        self.tavily_client = TavilyClient(api_key=tavily_api_key)

        try:
            logging.debug(f"Configuring MLflow for agent: {name}")
            mlflow.set_tracking_uri(mlflow_uri)
            mlflow.set_experiment("Agent Management")
        except Exception as e:
            logging.error(f"MLflow configuration failed: {e}")
            self.mlflow_enabled = False
        else:
            self.mlflow_enabled = True

        self.tools = self._initialize_tools()
        self.langchain_agent = initialize_agent(
            tools=self.tools, llm=self._openai_llm(), verbose=True
        )
        self.state_manager.set_state(self.name, "idle")

    def _openai_llm(self):
        from langchain.llms import OpenAI
        return OpenAI(temperature=0.7, model="gpt-4")

    def _initialize_tools(self):
        return [
            Tool(name="Notepad", func=self.reflect, description="Reflection tool."),
            Tool(name="Internet", func=self.search_internet, description="Search tool."),
        ]

    def reflect(self, input_text):
        self.state_manager.set_state(self.name, "reflecting")
        prompt = PromptTemplate(
            input_variables=["thoughts"],
            template="Reflect on these thoughts: {thoughts} Propose next steps."
        )
        chain = SequentialChain(chains=[], prompt=prompt)
        result = chain.run({"thoughts": input_text})
        self.state_manager.set_state(self.name, "idle")
        return result

    def search_internet(self, query):
        self.state_manager.set_state(self.name, "searching")
        try:
            response = self.tavily_client.search(query)
            results = response.get("results", [])
            if results:
                return "\n".join(f"{res['title']}: {res['content']}" for res in results[:3])
            return "No results found."
        except Exception as e:
            logging.error(f"Search failed: {e}")
            return f"Error: {e}"
        finally:
            self.state_manager.set_state(self.name, "idle")
