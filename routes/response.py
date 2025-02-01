from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class Response(BaseModel):
    message: str=''
     

@router.post("/")
def user_prompt(req: Response):
    content = req.message
    # will perform function in this
    return {"message": "System response"}

