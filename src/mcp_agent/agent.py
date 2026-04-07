from src.mcp_agent.tools.data_quality import check_null_revenue, check_missing_dates
from src.mcp_agent.tools.anomaly_detection import detect_revenue_drop


class MCPAgent:
    def __init__(self):
        self.name = "MCP Data Ops Agent"

    def handle_request(self, user_input: str):
        user_input = user_input.lower()

        if "null" in user_input:
            return check_null_revenue()

        elif "missing date" in user_input:
            return check_missing_dates()

        elif "revenue drop" in user_input or "anomaly" in user_input:
            return detect_revenue_drop()

        elif "pipeline" in user_input or "health" in user_input:
            return self.check_pipeline_health()

        else:
            return "Sorry, I don't understand the request."

    def check_pipeline_health(self):
        nulls = check_null_revenue()
        missing = check_missing_dates()
        anomalies = detect_revenue_drop()

        return {
            "null_issues": nulls.to_dict(orient="records"),
            "missing_dates": missing,
            "revenue_anomalies": anomalies
        }