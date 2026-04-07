from src.mcp_agent.tools.anomaly_detection import detect_revenue_drop

anomalies = detect_revenue_drop()

print("Revenue drop anomalies:")
for anomaly in anomalies:
    print(anomaly)