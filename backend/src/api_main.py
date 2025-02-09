import uvicorn
from fastapi import FastAPI, HTTPException
from uuid import uuid4, UUID
from pydantic import BaseModel
from core.agents.vars import embed_models_by_prov,chat_models_by_prov

app = FastAPI()
agents = {}

class Agent(BaseModel):
    name: str
    
@app.get("/get_models_by_provider")
async def get_models():
    return chat_models_by_prov

@app.get("/embed_models_by_prov")
async def get_models():
    return embed_models_by_prov

@app.post("/create_agent/", response_model=UUID)
async def create_agent(agent: Agent):
    agent_id = uuid4()
    agents[agent_id] = agent
    return agent_id

@app.get("/get_agent/{agent_id}", response_model=Agent)
async def get_agent(agent_id: UUID):
    if agent_id in agents:
        return agents[agent_id]
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

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)
