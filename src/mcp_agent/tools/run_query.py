import pandas as pd
from src.mcp_agent.database.connection import get_connection


def run_query(query: str) -> pd.DataFrame:
    conn = get_connection()
    try:
        df = pd.read_sql(query, conn)
        return df
    finally:
        conn.close()