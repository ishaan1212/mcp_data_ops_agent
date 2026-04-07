from src.mcp_agent.tools.execute_script import execute_script

result = execute_script("scripts/generate_data.py")

print(result["return_code"])
print(result["stdout"])
print(result["stderr"])