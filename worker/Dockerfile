# -------------------------
# Base image
# -------------------------
FROM python:3.11-slim

# -------------------------
# Set working directory
# -------------------------
WORKDIR /app

# -------------------------
# Install system dependencies (for compiling psycopg2, etc.)
# -------------------------
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        gcc g++ make curl unzip git wget ca-certificates && \
    rm -rf /var/lib/apt/lists/*

# -------------------------
# Copy requirements first for caching
# -------------------------
COPY requirements.txt ./ 

# -------------------------
# Install Python dependencies
# -------------------------
RUN pip install --no-cache-dir -r requirements.txt

# -------------------------
# Copy app code
# -------------------------
COPY worker.py ./

# -------------------------
# Optional: Create non-root user for security
# -------------------------
RUN useradd -ms /bin/bash appuser
USER appuser

# -------------------------
# Expose the port
# -------------------------
EXPOSE 2358

# -------------------------
# Start the worker with Gunicorn
# -------------------------
CMD ["gunicorn", "--bind", "0.0.0.0:2358", "--workers", "4", "worker:app", "redis"]
