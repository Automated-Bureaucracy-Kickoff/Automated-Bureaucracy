---
```markdown
# LangChain Middleware

## Overview

The **LangChain Middleware** is a custom middleware designed for FastAPI applications. It integrates the LangChain framework to analyze and log incoming HTTP requests dynamically. By leveraging LangChain's capabilities, this middleware generates meaningful summaries of request data, making it easier to monitor, debug, and enhance the overall observability of your backend system.

---

## Features

- **Dynamic Request Analysis**: Summarizes HTTP requests (method, path, headers) for better monitoring.
- **Customizable Logging**: Supports a configurable system prompt to define logging behavior.
- **LangChain Integration**: Utilizes `LLMChain` from LangChain for natural language processing of request data.
- **Error Handling**: Catches and logs errors during request processing to maintain system stability.

---

## Installation

1. Ensure you have the required dependencies:
   ```bash
   pip install fastapi starlette uvicorn openai langchain
   ```

2. Add the `LangChainMiddleware` to your FastAPI application.

---

## Usage

### Example Integration

Here's an example of how to integrate the `LangChainMiddleware`:

```python
from fastapi import FastAPI
from middleware.langchain.langchain_middleware import LangChainMiddleware

app = FastAPI()

# System prompt for the middleware
system_prompt = (
    "You are an AI middleware assistant. Analyze and log incoming HTTP requests, "
    "generating meaningful summaries for monitoring and debugging."
)

# OpenAI API Key
openai_api_key = "your_openai_api_key"

# Add the LangChainMiddleware
app.add_middleware(
    LangChainMiddleware,
    openai_api_key=openai_api_key,
    system_prompt=system_prompt,
)

@app.get("/")
async def root():
    return {"message": "Welcome to the LangChain Middleware Test API"}
```

### Running the Application

1. Save the above code as `main.py`.
2. Run the application:
   ```bash
   uvicorn main:app --reload
   ```

3. Access the application at [http://127.0.0.1:8000](http://127.0.0.1:8000).

---

## Configuration

The middleware can be customized using the following parameters:

- `openai_api_key`: Your OpenAI API key for accessing the LLM.
- `system_prompt`: A text-based prompt defining the middleware's behavior.

---

## How It Works

1. **Request Interception**: The middleware intercepts every incoming HTTP request.
2. **Request Analysis**: Extracts request details such as the method, path, and headers.
3. **LangChain Processing**: Passes the extracted data through a LangChain `LLMChain` to generate a summary.
4. **Logging**: Logs the summary message to the application's logging system.
5. **Response Forwarding**: Forwards the request to the next middleware or endpoint.

---

## Benefits

- Enhances **observability** by providing human-readable logs for debugging and analytics.
- Improves **monitoring** of API traffic with summarized request details.
- Reduces debugging effort through **structured and meaningful logging**.

---

## Limitations

- Relies on OpenAI API, which requires valid API credentials.
- Generates logs in natural language, which might need further parsing for machine-readability.

---

## Contributing

Contributions are welcome! If you encounter any issues or have ideas for improvement, feel free to submit a pull request or open an issue.

---
``` 

This `README.md` provides an overview, usage instructions, configuration options, and benefits of the `LangChainMiddleware`.