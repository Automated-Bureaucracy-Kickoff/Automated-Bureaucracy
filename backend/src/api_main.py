import uvicorn
from fastapi import FastAPI, HTTPException
from uuid import uuid4, UUID
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from core.agents.vars import embed_models_by_prov,chat_models_by_prov
from multi_agent import simulate_consciousness
app = FastAPI()
agents = {}

# it is a middleware to ensure that backend and frontend can communicate properly , if we not use this browser will not allow to share information b/w frontend and backend 
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],  
    allow_headers=["*"]
)

class Agent(BaseModel):
    name: str

class Multimodal_Agent_Parameter(BaseModel):
    system_prompt_analytica: str
    system_prompt_creativa: str
    system_prompt_pragmatica: str
    user_prompt: str
    
@app.get("/get_models_by_provider")
async def get_models():
    return {"message":chat_models_by_prov}

@app.get("/embed_models_by_prov")
async def get_models():
    return  {"message": embed_models_by_prov}

@app.post("/create_agent/", response_model=UUID)
async def create_agent(agent: Agent):
    agent_id = uuid4()
    agents[agent_id] = agent
    return   {"message": agent_id}

@app.get("/get_agent/{agent_id}", response_model=Agent)
async def get_agent(agent_id: UUID):
    if agent_id in agents:
        return  {"message": agents[agent_id]}
    else:
        raise HTTPException(status_code=404, detail="Agent not found")

@app.post("/interact_agent/{agent_id}")
async def interact_agent(agent_id: UUID, message: str):
    if agent_id in agents:
        agent = agents[agent_id]
        response = f"Agent {agent.name} received your message: {message}"
        return {"response": response}
    else:
        raise HTTPException(status_code=404, detail="Agent not found")

@app.post("/multiAgent")
async def interact_withMultiModalAgent(response:Multimodal_Agent_Parameter):
    data =  simulate_consciousness(response)
    return {"message":data} 
    

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
