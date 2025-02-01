from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import response  
from routes import settings
app = FastAPI()

origins = [
    "http://localhost:5173",  # Add your frontend URL
    "http://localhost",  # If you're using localhost without a port
]

# Add CORSMiddleware to the app
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # List of allowed origins
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],  # Allow all headers
)

# Root route
@app.get("/")
def read_root():
    return {"message": "Welcome to FastAPI!"}

# Include separate route files
app.include_router(response.router, prefix="/response", tags=["response"])
app.include_router(settings.router, prefix="/settings", tags=["setting"])


