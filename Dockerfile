# Use the official prebuilt Judge0 image
FROM judge0/judge0:latest

# Expose Judge0 API port
EXPOSE 2358

# Start Judge0 API
CMD ["./scripts/start.sh"]
