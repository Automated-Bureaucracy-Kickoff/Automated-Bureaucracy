from fastapi import APIRouter
from pydantic import BaseModel
from core.agents.chat.api_chat import api_Agent
from core.tools.search import search
from core.tools.pdf_loader import load_pdf, load_dir_of_pdfs
from langgraph.prebuilt import create_react_agent
from langgraph.checkpoint.memory import MemorySaver

router = APIRouter()

class Response(BaseModel):
    message: str=''
     

@router.post("/")
def user_prompt(req: Response):
    content = req.message
    agent = api_Agent("chat","google")
    agent.init_model("gemini-pro")
    tools = [search, load_pdf, load_dir_of_pdfs]
    memory = MemorySaver()
    agent = create_react_agent(agent.llm, tools ,checkpointer=memory)
    response =  agent.invoke(content)
    return {"message": response}