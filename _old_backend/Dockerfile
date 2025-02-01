# Base image
FROM python:3.10-slim

# Set the working directory inside the container
WORKDIR /app

# Copy only requirements to leverage Docker's caching mechanism
COPY ./backend/requirements.txt /app/requirements.txt

# Install dependencies
RUN pip install --no-cache-dir -r /app/requirements.txt

# Copy the entire backend directory into the container
COPY ./backend /app

# Expose the port the application runs on
EXPOSE 8000

# Define environment variables
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

# Command to run the application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
