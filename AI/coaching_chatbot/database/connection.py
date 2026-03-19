# coaching_chatbot/database/connection.py
import psycopg2
from psycopg2.pool import SimpleConnectionPool
from pgvector.psycopg2 import register_vector
from contextlib import contextmanager
from config.settings import DATABASE_URL
import atexit

db_pool = None
if DATABASE_URL:
    try:
        db_pool = SimpleConnectionPool(
            1, 20,
            DATABASE_URL
        )
        
        # Register pgvector globally so ALL connections in the pool understand vectors
        conn = db_pool.getconn()
        register_vector(conn, globally=True)
        db_pool.putconn(conn)
    except Exception as e:
        print(f"Failed to initialize database pool: {e}")

def get_db():
    if not db_pool:
        raise Exception("Database connection pool not initialized.")
    conn = db_pool.getconn()
    try:
        yield conn
    except Exception:
        conn.rollback()
        raise
    finally:
        # Prevent poisoned connections from going back into the pool
        conn.rollback()
        db_pool.putconn(conn)

def close_pool():
    if db_pool:
        db_pool.closeall()

atexit.register(close_pool)
