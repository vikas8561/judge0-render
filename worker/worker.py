import os
import psycopg2
from flask import Flask

app = Flask(__name__)

# Connect to Render Postgres using internal URL
DATABASE_URL = os.environ.get("DATABASE_URL")

try:
    conn = psycopg2.connect(DATABASE_URL)
    print("✅ Connected to the database successfully")
except Exception as e:
    print("❌ DB connection failed:", e)
    exit(1)

@app.route("/")
def home():
    return "Judge0 Worker running!"

if __name__ == "__main__":
    port = int(os.environ.get("WORKER_PORT", 2358))
    app.run(host="0.0.0.0", port=port)
