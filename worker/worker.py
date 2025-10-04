import os
import logging
from flask import Flask
from psycopg2 import pool, PoolError

# -------------------------
# Logging setup
# -------------------------
logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")

# -------------------------
# Flask app
# -------------------------
app = Flask(__name__)

# -------------------------
# Database connection pool
# -------------------------
DATABASE_URL = os.environ.get("DATABASE_URL")
if not DATABASE_URL:
    logging.error("DATABASE_URL environment variable not set")
    raise RuntimeError("DATABASE_URL environment variable not set")

try:
    db_pool = pool.SimpleConnectionPool(
        minconn=5,
        maxconn=20,
        dsn=DATABASE_URL
    )
    if db_pool:
        logging.info("✅ Connection pool created successfully")
except Exception as e:
    logging.error(f"❌ DB connection pool creation failed: {e}")
    raise

# Graceful shutdown of pool
import atexit
@atexit.register
def close_pool():
    if db_pool:
        db_pool.closeall()
        logging.info("🔒 Connection pool closed")

# -------------------------
# Routes
# -------------------------
@app.route("/")
def home():
    conn = None
    try:
        conn = db_pool.getconn()
        if not conn:
            return "All database connections are busy, try again later.", 503

        with conn.cursor() as cur:
            cur.execute("SELECT NOW();")
            result = cur.fetchone()

        return f"Judge0 Worker running! DB time: {result[0]}"

    except PoolError:
        return "All database connections are busy, try again later.", 503
    except Exception as e:
        logging.error(f"DB query failed: {e}")
        return f"DB query failed: {e}", 500
    finally:
        if conn:
            db_pool.putconn(conn)

# -------------------------
# Main entry
# -------------------------
if __name__ == "__main__":
    port = int(os.environ.get("WORKER_PORT", 2358))
    # Dev server only; in production use Gunicorn
    logging.info(f"🚀 Starting Flask dev server on 0.0.0.0:{port}")
    app.run(host="0.0.0.0", port=port)
