import os
import psycopg2
from psycopg2 import pool
from flask import Flask

app = Flask(__name__)

# Connect to Render Postgres using internal URL with connection pooling
DATABASE_URL = os.environ.get("DATABASE_URL")

try:
    db_pool = pool.SimpleConnectionPool(
        minconn=5,
        maxconn=20,
        dsn=DATABASE_URL
    )
    if db_pool:
        print("✅ Connection pool created successfully")
except Exception as e:
    print("❌ DB connection pool creation failed:", e)
    exit(1)


@app.route("/")
def home():
    # Example usage of connection pool
    conn = None
    try:
        conn = db_pool.getconn()
        cur = conn.cursor()
        cur.execute("SELECT NOW();")  # simple test query
        result = cur.fetchone()
        cur.close()
        return f"Judge0 Worker running! DB time: {result[0]}"
    except Exception as e:
        return f"DB query failed: {e}"
    finally:
        if conn:
            db_pool.putconn(conn)


if __name__ == "__main__":
    port = int(os.environ.get("WORKER_PORT", 2358))
    # For production, use a WSGI server like Gunicorn instead of Flask dev server
    app.run(host="0.0.0.0", port=port)
