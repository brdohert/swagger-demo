# Use Python 3.11 slim image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONPATH=/app

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Create non-root user
RUN useradd -m appuser && chown -R appuser:appuser /app
USER appuser

# Expose port
EXPOSE 8000

# Run the applicationhttp://localhost:8080http://localhost:8080
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]

# Base image: Uses Python 3.9 with a slim variant to minimize image size
# WORKDIR: Sets the working directory inside the container to /app
# COPY requirements.txt: Copies the requirements.txt file from host to container
# RUN pip install: Installs Python dependencies from requirements.txt
#   --no-cache-dir: Prevents caching pip packages to reduce image size
# COPY . .: Copies all files from current directory to container's /app
# CMD: Runs uvicorn server when container starts
#   --host 0.0.0.0: Allows external connections
#   --port 8000: Sets server port
#   --reload: Enables auto-reload on code changes (development mode) 