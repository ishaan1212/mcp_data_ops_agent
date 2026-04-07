from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
print("API KEY LOADED:", api_key is not None)

client = OpenAI(api_key=api_key)

response = client.responses.create(
    model="gpt-4.1-mini",
    input="Say hello in one sentence"
)

print(response.output_text)