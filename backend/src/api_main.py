from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from core.routes import response  
from core.routes import settings
app = FastAPI()

origins = [
    "http://localhost:5173"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins, 
    allow_credentials=True,
    allow_methods=["*"],  
    allow_headers=["*"]
)

@app.get("/")
def read_root():
    return {"message": "Welcome to FastAPI!"}

app.include_router(response.router, prefix="/response", tags=["response"])
app.include_router(settings.router, prefix="/settings", tags=["setting"])