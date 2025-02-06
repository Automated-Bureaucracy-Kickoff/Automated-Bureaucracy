from fastapi import APIRouter
from pydantic import BaseModel
from core.agents.chat.api_chat import api_Agent
from core.tools.search import search
from core.tools.pdf_loader import load_pdf, load_dir_of_pdfs
from langgraph.prebuilt import create_react_agent
from langgraph.checkpoint.memory import MemorySaver
from langchain_core.messages import HumanMessage

router = APIRouter()

class Response(BaseModel):
    message: str=''
     

@router.post("/")
def user_prompt(req: Response):
    # Assume req.message is the input string
    content = req.message  
    agent = api_Agent("chat", "google")
    agent.init_model("gemini-pro")
    tools = [search, load_pdf, load_dir_of_pdfs]

    # Initialize and configure the MemorySaver checkpointer
    memory = MemorySaver()
    memory.thread_id = "my_thread"
    
    # Create the react agent with the checkpointer
    agent = create_react_agent(agent.llm, tools, checkpointer=memory)
    
    # Provide the configuration with the thread_id for persistence
    config = {"configurable": {"thread_id": "my_thread"}}
    
    # Invoke the agent; ensure the input is in the expected format.
    # If your graph expects a dict (e.g., with a "messages" key), adjust accordingly.
    # For example, if your agent expects a state dict:
    input_state = {"messages": [content]}
    
    raw_response = agent.invoke(input_state, config=config)
    
    # Check if the output is a dict; if it's not, wrap it accordingly.
    if not isinstance(raw_response, dict):
        response = {"messages": [raw_response]}
    else:
        response = raw_response

    return {"message": response}

