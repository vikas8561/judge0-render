# Use the official prebuilt Judge0 image
FROM judge0/judge0:latest

# Fix ownership of lua directory to avoid chown issues
RUN chown -R 0:0 /usr/local/lua-5.3.5

# Create /box directory for isolate sandbox
RUN mkdir -p /box

# Expose the API port
EXPOSE 2358
