from src.mcp_agent.tools.run_query import run_query

query = """
SELECT *
FROM revenue_data
LIMIT 5
"""

df = run_query(query)
print(df)