# -------------------------
# Base image
# -------------------------
FROM python:3.11-slim

# -------------------------
# Set working directory
# -------------------------
WORKDIR /app

# -------------------------
# Install system dependencies (for compiling psycopg2, isolate, etc.)
# -------------------------
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        gcc g++ make curl unzip git wget ca-certificates && \
    rm -rf /var/lib/apt/lists/*

# -------------------------
# Install isolate for sandboxing code execution
# -------------------------
RUN git clone https://github.com/ioi/isolate.git /tmp/isolate && \
    cd /tmp/isolate && \
    make isolate && \
    make install && \
    rm -rf /tmp/isolate

# -------------------------
# Create /box directory for isolate sandbox
# -------------------------
RUN mkdir -p /box

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
# Run as root for isolate (requires root privileges)
# -------------------------

# -------------------------
# Expose the port
# -------------------------
EXPOSE 2358

# -------------------------
# Start the worker with Gunicorn
# -------------------------
CMD ["gunicorn", "--bind", "0.0.0.0:2358", "--workers", "4", "worker:app", "redis"]
