from src.mcp_agent.tools.data_quality import check_null_revenue, check_missing_dates
from src.mcp_agent.tools.anomaly_detection import detect_revenue_drop
from src.mcp_agent.tools.execute_script import execute_script
from src.mcp_agent.tools.database_delete import delete_database
from src.mcp_agent.LLM.router import route_request


class MCPAgent:

    def check_pipeline_health(self):
        return {
            "nulls": check_null_revenue().to_dict(orient="records"),
            "missing_dates": check_missing_dates(),
            "anomalies": detect_revenue_drop()
        }

    def handle_request(self, user_input: str):
        decision = route_request(user_input)

        tool = decision["tool_name"]

        if tool == "check_null_revenue":
            return check_null_revenue().to_dict(orient="records")

        elif tool == "check_missing_dates":
            return check_missing_dates()

        elif tool == "detect_revenue_drop":
            return detect_revenue_drop()

        elif tool == "check_pipeline_health":
            return self.check_pipeline_health()

        elif tool == "execute_generate_data":
            return execute_script("scripts/generate_data.py")
        
        # elif tool == "database_delete":
        #     return delete_database()

        else:
            return {"error": "Unknown tool", "decision": decision}