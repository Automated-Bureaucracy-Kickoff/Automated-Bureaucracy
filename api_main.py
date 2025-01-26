from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Any

app = FastAPI()

class AgentSettings(BaseModel):
    temperature: float
    max_tokens: int

class AgentPrompt(BaseModel):
    prompt: str
    response: Any
    


# Function to set agent settings
def set_agent_settings(settings: AgentSettings):
    global current_agent_settings
    current_agent_settings = settings
    return current_agent_settings

@app.post("/set-settings/")
async def set_settings(settings: AgentSettings):
    try:
        updated_settings = set_agent_settings(settings)
        return {"message": "Settings updated successfully", "settings": updated_settings}
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Failed to update settings: {e}")


