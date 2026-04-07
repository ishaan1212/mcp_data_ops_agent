from src.mcp_agent.tools.run_query import run_query


def detect_revenue_drop(threshold: float = 0.5):
    query = """
    SELECT date, region, revenue
    FROM revenue_data
    ORDER BY date
    """
    df = run_query(query)

    anomalies = []

    grouped = df.groupby("region")

    for region, group in grouped:
        group = group.sort_values("date").reset_index(drop=True)

        for i in range(1, len(group)):
            previous_revenue = group.loc[i - 1, "revenue"]
            current_revenue = group.loc[i, "revenue"]
            current_date = group.loc[i, "date"]

            if previous_revenue and current_revenue is not None:
                if current_revenue < previous_revenue * threshold:
                    anomalies.append(
                        {
                            "date": current_date,
                            "region": region,
                            "previous_revenue": previous_revenue,
                            "current_revenue": current_revenue,
                        }
                    )

    return anomalies