import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import sqlite3
import os

os.makedirs("data", exist_ok=True)

start_date = datetime(2025, 1, 1)
days = 60
regions = ["East", "West", "North", "South"]

data = []

for i in range(days):
    current_date = start_date + timedelta(days=i)

    for region in regions:
        revenue = np.random.randint(800, 1500)
        customers = np.random.randint(20, 80)

        data.append(
            [
                current_date.strftime("%Y-%m-%d"),
                region,
                revenue,
                customers
            ]
        )

df = pd.DataFrame(data, columns=["date", "region", "revenue", "customers"])

# Inject anomaly 1: remove some dates entirely
df = df[~df["date"].isin(["2025-01-15", "2025-01-28"])]

# Inject anomaly 2: sudden revenue drop in one region
df.loc[
    (df["date"] == "2025-02-10") & (df["region"] == "West"),
    "revenue"
] = 200

# Inject anomaly 3: null revenue value
df.loc[
    (df["date"] == "2025-02-05") & (df["region"] == "South"),
    "revenue"
] = None

conn = sqlite3.connect("data/agent.db")
df.to_sql("revenue_data", conn, if_exists="replace", index=False)
conn.close()

print("Data generated and stored in SQLite successfully.")