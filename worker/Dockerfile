# Dockerfile for Judge0 Worker
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install system dependencies (for compiling languages)
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        gcc g++ make curl unzip git wget ca-certificates && \
    rm -rf /var/lib/apt/lists/*

# Copy worker code and requirements
COPY requirements.txt ./
COPY worker.py ./
COPY other_files_or_folders ./other_files_or_folders

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port the worker listens on
EXPOSE 2358

# Start the worker
CMD ["python", "worker.py"]
