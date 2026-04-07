import json
from pathlib import Path
from openai import OpenAI # type: ignore
from src.mcp_agent.config import OPENAI_API_KEY


def load_prompt():
    path = Path("src/mcp_agent/prompts/router_prompts.txt")
    return path.read_text()


def route_request(user_input: str):
    client = OpenAI(api_key=OPENAI_API_KEY)

    system_prompt = load_prompt()

    response = client.responses.create(
        model="gpt-4.1-mini",
        input=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_input}
        ]
    )

    output = response.output_text.strip()

    print('RAW OUTPUT')
    print(output)

    return json.loads(output)