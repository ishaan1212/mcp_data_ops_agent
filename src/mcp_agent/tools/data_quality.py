from src.mcp_agent.tools.run_query import run_query


def check_null_revenue():
    query = """
    SELECT *
    FROM revenue_data
    WHERE revenue IS NULL
    """
    return run_query(query)


def check_missing_dates():
    query = """
    SELECT DISTINCT date
    FROM revenue_data
    ORDER BY date
    """
    df = run_query(query)

    dates = df["date"].tolist()

    missing_dates = []
    for i in range(len(dates) - 1):
        current_date = dates[i]
        next_date = dates[i + 1]

        current_day = int(current_date[-2:])
        next_day = int(next_date[-2:])

        if next_day - current_day > 1 and current_date[:7] == next_date[:7]:
            for missing_day in range(current_day + 1, next_day):
                missing_dates.append(f"{current_date[:8]}{missing_day:02d}")

    return missing_dates