from src.mcp_agent.tools.data_quality import check_null_revenue, check_missing_dates

print("Null revenue rows:")
print(check_null_revenue())

print("\nMissing dates:")
print(check_missing_dates())