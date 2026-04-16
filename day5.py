from dotenv import load_dotenv
import os
import requests

load_dotenv()

api_key = os.getenv("ANTHROPIC_API_KEY")

response = requests.post(
    "https://api.anthropic.com/v1/messages",
    headers={
        "x-api-key": api_key,
        "anthropic-version": "2023-06-01",
        "content-type": "application/json"
    },
    json={
        "model": "claude-haiku-4-5-20251001",
        "max_tokens": 100,
        "messages": [
            {"role": "user", "content": "Say hello in one sentence."}
        ]
    }
)

data = response.json()
print(data)
print(data["content"][0]["text"])