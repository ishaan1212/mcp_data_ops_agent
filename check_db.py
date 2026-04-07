import sqlite3
import pandas as pd

conn = sqlite3.connect("data/agent.db")

print("Sample rows:")
print(pd.read_sql("SELECT * FROM revenue_data LIMIT 8", conn))

print("\nCheck for missing dates:")
dates_df = pd.read_sql("""
    SELECT DISTINCT date
    FROM revenue_data
    ORDER BY date
""", conn)
print(dates_df.head(20))

print("\nCheck sudden revenue drop:")
drop_df = pd.read_sql("""
    SELECT *
    FROM revenue_data
    WHERE date = '2025-02-10' AND region = 'West'
""", conn)
print(drop_df)

print("\nCheck null revenue:")
null_df = pd.read_sql("""
    SELECT *
    FROM revenue_data
    WHERE date = '2025-02-05' AND region = 'South'
""", conn)
print(null_df)

conn.close()