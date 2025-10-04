# Use the official prebuilt Judge0 image
FROM judge0/judge0:latest

# Run as root for isolate (requires root privileges)
USER root

# Create /box directory for isolate sandbox
RUN mkdir -p /box

# Expose the API port
EXPOSE 2358
