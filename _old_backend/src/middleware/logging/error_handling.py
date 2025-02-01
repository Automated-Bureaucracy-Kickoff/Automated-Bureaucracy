"""
error_handling.py

Middleware for handling and logging errors in FastAPI applications.
"""

from fastapi import Request, Response
from fastapi.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware
import logging

# Configure logging for error handling
logger = logging.getLogger("error_handling")
logger.setLevel(logging.ERROR)
handler = logging.StreamHandler()
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
handler.setFormatter(formatter)
logger.addHandler(handler)


class ErrorHandlingMiddleware(BaseHTTPMiddleware):
    """
    Middleware to handle exceptions and provide structured error responses.
    """

    async def dispatch(self, request: Request, call_next):
        """
        Intercepts HTTP requests and handles errors.

        Args:
            request (Request): The incoming HTTP request.
            call_next (callable): The next middleware or endpoint to handle the request.

        Returns:
            Response: The HTTP response, or an error response if an exception occurs.
        """
        try:
            # Proceed with the request and get the response
            response = await call_next(request)
            return response
        except Exception as e:
            # Log the error
            logger.error("An error occurred: %s", str(e), exc_info=True)

            # Return a structured JSON error response
            error_response = {
                "error": "An unexpected error occurred.",
                "details": str(e),
            }
            return JSONResponse(status_code=500, content=error_response)


# Example usage in a FastAPI application
if __name__ == "__main__":
    from fastapi import FastAPI

    app = FastAPI()

    # Add the error-handling middleware
    app.add_middleware(ErrorHandlingMiddleware)

    @app.get("/")
    async def root():
        return {"message": "Welcome to the Error Handling Middleware Test API"}

    @app.get("/error")
    async def trigger_error():
        raise ValueError("This is a test error!")

    # Run the application using Uvicorn
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
