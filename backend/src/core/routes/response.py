from fastapi import APIRouter
from pydantic import BaseModel
from core.agents.api_agent import api_Agent

router = APIRouter()

class Response(BaseModel):
    message: str=''
     

@router.post("/")
def user_prompt(req: Response):
    content = req.message
    agent = api_Agent("chat","google")
    agent.init_model("gemini-pro")
    response =  agent.llm.invoke(content)
    return {"message": response}