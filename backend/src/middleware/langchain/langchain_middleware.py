from fastapi import Request, HTTPException
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import Response
import logging
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.llms import OpenAI

class LangChainMiddleware(BaseHTTPMiddleware):
    """
    Middleware for processing incoming requests through LangChain for logging and dynamic task handling.
    """

    def __init__(self, app, openai_api_key: str, system_prompt: str):
        super().__init__(app)
        self.openai_api_key = openai_api_key
        self.system_prompt = system_prompt
        self.llm = OpenAI(api_key=openai_api_key)
        self.prompt_template = PromptTemplate(
            input_variables=["method", "path", "headers"],
            template=(
                "{system_prompt}\n\n"
                "Incoming Request Details:\n"
                "Method: {method}\n"
                "Path: {path}\n"
                "Headers: {headers}\n\n"
                "Generate a brief log message summarizing this request."
            ),
        )
        self.chain = LLMChain(llm=self.llm, prompt=self.prompt_template)
        self.logger = logging.getLogger("LangChainMiddleware")

    async def dispatch(self, request: Request, call_next):
        """
        Intercept and process the request using LangChain before passing it to the endpoint.
        """
        try:
            # Extract request details
            method = request.method
            path = request.url.path
            headers = dict(request.headers)

            # Use LangChain to generate a log message
            log_message = self.chain.run(
                {
                    "method": method,
                    "path": path,
                    "headers": str(headers),
                    "system_prompt": self.system_prompt,
                }
            )

            # Log the generated message
            self.logger.info(f"LangChain Log: {log_message}")

            # Pass the request to the next middleware or endpoint
            response = await call_next(request)
            return response

        except Exception as e:
            # Handle errors gracefully
            self.logger.error(f"LangChainMiddleware Error: {e}")
            raise HTTPException(status_code=500, detail="Internal Middleware Error")

# Example usage
if __name__ == "__main__":
    from fastapi import FastAPI
    import uvicorn

    app = FastAPI()

    system_prompt = (
        "You are an AI middleware assistant. Analyze and log incoming HTTP requests, "
        "generating meaningful summaries for monitoring and debugging."
    )
    openai_api_key = "your_openai_api_key"

    app.add_middleware(
        LangChainMiddleware,
        openai_api_key=openai_api_key,
        system_prompt=system_prompt,
    )

    @app.get("/")
    async def root():
        return {"message": "Welcome to the LangChain Middleware Test API"}

    uvicorn.run(app, host="127.0.0.1", port=8000)
