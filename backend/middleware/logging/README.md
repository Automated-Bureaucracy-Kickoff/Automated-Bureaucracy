### `README.md`

# Logging Middleware

## Overview
The Logging Middleware module provides centralized logging capabilities for FastAPI applications. It captures and logs details of incoming requests and outgoing responses, enabling efficient monitoring, debugging, and troubleshooting of API activity.

---

## Features
1. **Request Logging**:
   - Logs HTTP method, URL, and request headers for all incoming requests.
   - Records the timestamp of each request.

2. **Response Logging**:
   - Logs HTTP status codes and headers of outgoing responses.
   - Tracks the total processing time for each request.

3. **Error Handling**:
   - Captures and logs exceptions raised during request handling, along with stack traces.

4. **Customizable**:
   - The middleware uses Python's `logging` module, making it easy to integrate with external log aggregators like ELK Stack, Datadog, or Splunk.

---

## File Structure
```
logging/
├── error_handling.py       # Handles error-specific logging
├── logging_middleware.py   # Middleware implementation for request/response logging
└── README.md               # Documentation for the logging middleware
```

---

## `logging_middleware.py`

### Purpose
This file implements the `LoggingMiddleware` class, which extends FastAPI's `BaseHTTPMiddleware` to intercept and log HTTP request/response cycles.

### Usage
To integrate the middleware into your FastAPI app:
```python
from fastapi import FastAPI
from middleware.logging.logging_middleware import LoggingMiddleware

app = FastAPI()

# Add the logging middleware
app.add_middleware(LoggingMiddleware)

@app.get("/")
async def root():
    return {"message": "Hello, Logging Middleware!"}
```

---

## `error_handling.py`

### Purpose
Contains utility functions and handlers for logging errors and exceptions during request processing.

### Key Features
- Provides structured error logs with detailed stack traces.
- Ensures consistent logging across the application.

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/automatedbureaucracy.git
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the application with logging enabled:
   ```bash
   uvicorn backend.middleware.logging.logging_middleware:app --reload
   ```

---

## Log Format
The logs are structured and include the following details:

1. **Request Logs**:
   - Timestamp
   - HTTP Method
   - Request URL
   - Request Headers

   Example:
   ```plaintext
   2025-01-25 21:15:00 - INFO - Incoming request: GET http://127.0.0.1:8000/
   2025-01-25 21:15:00 - INFO - Headers: {'host': '127.0.0.1:8000', 'user-agent': 'curl/7.68.0', ...}
   ```

2. **Response Logs**:
   - HTTP Status Code
   - Response Headers
   - Processing Time

   Example:
   ```plaintext
   2025-01-25 21:15:00 - INFO - Outgoing response: 200 - Process time: 0.01 seconds
   2025-01-25 21:15:00 - INFO - Response headers: {'content-length': '39', 'content-type': 'application/json'}
   ```

3. **Error Logs**:
   - Exception type and message
   - Stack trace

   Example:
   ```plaintext
   2025-01-25 21:15:01 - ERROR - Error during request processing: ValueError: Invalid input
   Traceback (most recent call last):
     File "app.py", line 20, in example_handler
       raise ValueError("Invalid input")
   ```

---

## Future Enhancements
- **Structured Logging**: Integrate JSON logging for compatibility with log aggregators.
- **Distributed Tracing**: Add support for tracing requests across microservices.
- **Dynamic Log Levels**: Allow configuration of log levels through environment variables.

---

## Support
For any questions or issues, please contact:
- Email: [blakedehaas@automatedbureaucracy.com](mailto:blakedehaas@automatedbureaucracy.com)
- GitHub Issues: [GitHub Repository](https://github.com/automatedbureaucracy/issues) 

--- 