import os
from dotenv import load_dotenv
import openai
from langchain.agents import Tool
from tavily import TavilyClient
from .agent_state_manager import AgentStateManager


class Agent:
    """
    Represents an intelligent agent with OpenAI o1-mini integration and Tavily.
    """

    def __init__(
        self,
        name: str,
        system_prompt: str,
        openai_api_key: str = None,
        tavily_api_key: str = None,
        message_bus=None
    ):
        """
        Initialize the agent with required configurations and optional MessageBus integration.

        If openai_api_key is not provided, the code will load it from a .env file using python-dotenv.
        """
        self.name = name
        self.system_prompt = system_prompt
        self.state_manager = AgentStateManager()

        # If no TAVILY_API_KEY is provided, fallback to environment
        if not tavily_api_key:
            tavily_api_key = os.environ.get("TAVILY_API_KEY", "")
        self.tavily_client = TavilyClient(api_key=tavily_api_key)
        self.message_bus = message_bus

        # Load environment variables from .env
        load_dotenv()

        # If no openai_api_key is passed, fallback to environment variable
        if not openai_api_key:
            openai_api_key = os.environ.get("OPENAI_API_KEY", "")
        # Configure the API key (module-level usage)
        openai.api_key = openai_api_key

        if self.message_bus:
            self.message_bus.register(self.name, self._process_message)

        self.tools = self._initialize_tools()
        self.state_manager.set_state(self.name, "idle")

    def _o1_mini_llm(self, prompt: str) -> str:
        """
        Uses the OpenAI library call for chat completions with the o1-mini model.
        o1-mini does not support the "system" role, so we rename it to "assistant".
        """
        try:
            response = openai.chat.completions.create(
                model="o1-mini",
                messages=[
                    {"role": "assistant", "content": self.system_prompt},
                    {"role": "user", "content": prompt},
                ],
                n=1,
                stop=["\nObservation:"],
            )
            return response.choices[0].message.content
        except Exception as e:
            raise e

    def _initialize_tools(self):
        """
        Sets up the tools available to the agent.
        """
        return [
            Tool(name="Notepad", func=self.reflect, description="Tool for reflection."),
            Tool(name="Internet", func=self.search_internet, description="Tool for internet search."),
        ]

    def reflect(self, input_text: str) -> str:
        """
        A tool for reflecting on input text and proposing next steps.
        """
        self.state_manager.set_state(self.name, "reflecting")
        try:
            prompt = f"Reflect on the following thoughts: {input_text}. Propose next steps."
            result = self._o1_mini_llm(prompt)
            return result
        except Exception as e:
            return f"Error during reflection: {e}"
        finally:
            self.state_manager.set_state(self.name, "idle")

    def search_internet(self, query: str) -> str:
        """
        A tool for searching the internet.
        """
        self.state_manager.set_state(self.name, "searching")
        try:
            response = self.tavily_client.search(query)
            results = response.get("results", [])
            if results:
                formatted_results = "\n".join(
                    f"{res['title']}: {res['content']}" for res in results[:3]
                )
                return formatted_results
            return "No results found."
        except Exception as e:
            return f"Error during search: {e}"
        finally:
            self.state_manager.set_state(self.name, "idle")

    def execute_task(self, prompt: str) -> str:
        """
        Executes a task based on the provided prompt.
        """
        try:
            response = self._o1_mini_llm(prompt)
            return response
        except Exception as e:
            raise e

    def send_message(self, message: str) -> None:
        """
        Publishes a message to the MessageBus.
        """
        if self.message_bus:
            self.message_bus.publish(signal="message", sender=self.name, message=message)

    def _process_message(self, signal: str, message: str, sender: str) -> None:
        """
        Processes a message received via the MessageBus.
        """
        if signal == "message":
            try:
                response = self.execute_task(message)
                self.send_message(response)
            except Exception as e:
                pass
