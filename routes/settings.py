from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class Setting(BaseModel):
    settings: object 


@router.get("/")
def get_setting():
    return {"Settings": "we don't need this though , in frontend settings can be stored in local storage"}


@router.post("/")
def append_setting(req: Setting):
    content = req.settings
    return {"message": "Settings created!",content:content}
