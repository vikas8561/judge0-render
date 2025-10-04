import os
import time
import psycopg2
import requests

# Database configuration
DB_HOST = os.getenv("DB_HOST")
DB_PORT = int(os.getenv("DB_PORT", 5432))
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")

def connect_db():
    try:
        conn = psycopg2.connect(
            host=DB_HOST,
            port=DB_PORT,
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD
        )
        print("Connected to DB successfully")
        return conn
    except Exception as e:
        print(f"DB connection failed: {e}")
        return None

def worker_loop():
    conn = connect_db()
    if not conn:
        return
    
    while True:
        # Example: fetch a job (replace with actual Judge0 logic)
        print("Worker running...")
        time.sleep(5)  # simulate doing work

if __name__ == "__main__":
    worker_loop()
