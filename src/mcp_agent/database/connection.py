import sqlite3
from src.mcp_agent.config import DB_PATH


def get_connection():
    return sqlite3.connect(DB_PATH)