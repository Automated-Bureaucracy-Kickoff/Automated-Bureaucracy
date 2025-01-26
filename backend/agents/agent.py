import openai
from langchain.chains import SequentialChain
from langchain.prompts import PromptTemplate
from langchain.agents import Tool, initialize_agent
from langchain.agents.agent_toolkits import create_tools_agent
from langchain.memory import ConversationBufferMemory
from tavily import TavilyAPI
import mlflow


class Agent:
    """
    Represents an intelligent agent with OpenAI, LangChain, Tavily integration, and model tracking via MLflow.
    """

    def __init__(self, name, system_prompt, openai_api_key, tavily_api_key, mlflow_uri):
        """
        Initializes the agent.

        Args:
            name (str): Name of the agent.
            system_prompt (str): System prompt defining the agent's behavior.
            openai_api_key (str): OpenAI API key.
            tavily_api_key (str): Tavily API key for internet access.
            mlflow_uri (str): URI for the MLflow server.
        """
        self.name = name
        self.system_prompt = system_prompt
        self.memory = ConversationBufferMemory(memory_key="history")
        self.openai_api_key = openai_api_key
        self.tavily = TavilyAPI(api_key=tavily_api_key)

        # Configure MLflow
        mlflow.set_tracking_uri(mlflow_uri)
        mlflow.set_experiment("Agent Management")

        # Initialize OpenAI API
        openai.api_key = openai_api_key

        # Define tools for the agent
        self.tools = self.initialize_tools()

        # Define LangChain agent with tools and memory
        self.langchain_agent = initialize_agent(
            tools=self.tools,
            llm=self.openai_llm(),
            memory=self.memory,
            verbose=True,
        )

    def openai_llm(self):
        """
        Creates an OpenAI-based language model for the agent.

        Returns:
            OpenAI model instance.
        """
        from langchain.llms import OpenAI
        return OpenAI(temperature=0.7, model="gpt-4")

    def initialize_tools(self):
        """
        Sets up tools available to the agent.

        Returns:
            list of Tool: Tools for reflection and internet access.
        """
        return [
            Tool(
                name="Notepad",
                func=self.reflect,
                description="Use this tool to store thoughts and perform self-prompting reflection.",
            ),
            Tool(
                name="Internet",
                func=self.search_internet,
                description="Use this tool to search the web for real-time information.",
            ),
        ]

    def reflect(self, input_text):
        """
        Simulates a notepad for reflection and self-prompting.

        Args:
            input_text (str): Input thought or reflection to process.

        Returns:
            str: Reflection response.
        """
        self.memory.add_memory(input_text)
        reflection_prompt = PromptTemplate(
            input_variables=["thoughts"],
            template="""
                Reflect on the following thoughts:
                {thoughts}
                Based on this reflection, propose actionable next steps.
            """,
        )
        chain = SequentialChain(chains=[], prompt=reflection_prompt)
        return chain.run({"thoughts": input_text})

    def search_internet(self, query):
        """
        Uses Tavily API for web search.

        Args:
            query (str): Query string to search the internet.

        Returns:
            str: Search result summary.
        """
        try:
            response = self.tavily.search(query)
            return response.get("summary", "No summary available.")
        except Exception as e:
            return f"Error accessing the internet: {e}"

    def execute_task(self, task_prompt):
        """
        Executes a task using LangChain workflows.

        Args:
            task_prompt (str): Prompt defining the task.

        Returns:
            str: Task output from the LangChain agent.
        """
        return self.langchain_agent.run(input=task_prompt)

    def log_model(self, model_name, params, metrics):
        """
        Logs model metadata to MLflow.

        Args:
            model_name (str): Name of the model.
            params (dict): Model parameters.
            metrics (dict): Model performance metrics.
        """
        with mlflow.start_run():
            mlflow.log_params(params)
            mlflow.log_metrics(metrics)
            mlflow.set_tag("model_name", model_name)

    def get_memory(self):
        """
        Retrieves the agent's memory log.

        Returns:
            list: List of memory entries.
        """
        return self.memory.load_memory()


# Example Usage
if __name__ == "__main__":
    agent = Agent(
        name="Agent1",
        system_prompt="You are an assistant specializing in summarization and analysis.",
        openai_api_key="your_openai_api_key",
        tavily_api_key="your_tavily_api_key",
        mlflow_uri="http://localhost:5000",
    )

    # Example Task Execution
    result = agent.execute_task("Summarize the latest trends in AI research.")
    print(f"Task Result: {result}")

    # Internet Search Example
    search_result = agent.search_internet("Latest advancements in quantum computing.")
    print(f"Internet Search Result: {search_result}")

    # Reflection Example
    reflection_result = agent.reflect("How can we optimize AI for creative tasks?")
    print(f"Reflection Result: {reflection_result}")

    # Model Logging Example
    agent.log_model(
        model_name="AI Summarizer",
        params={"temperature": 0.7, "model": "gpt-4"},
        metrics={"accuracy": 0.95, "f1_score": 0.92},
    )
