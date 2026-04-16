from dotenv import load_dotenv
import os
import requests

load_dotenv()

api_key = os.getenv("ANTHROPIC_API_KEY")

def ask_claude(question):
    response = requests.post(
    "https://api.anthropic.com/v1/messages",
    headers={
        "x-api-key": api_key,
        "anthropic-version": "2023-06-01",
        "content-type": "application/json"
    },
    json={
        "model": "claude-haiku-4-5-20251001",
        "max_tokens": 200,
        "system": "You are Egor's personal assistant. You are helpful, direct and brief.",
        "messages": [
            {"role": "user", "content": question}
        ]
    }
) 
    data = response.json()
    return data["content"][0]["text"]

while True:
    user_input = input("You: ")
    if user_input.lower() == "quit":
        break
    response = ask_claude(user_input)
    print(f"Assistant: {response}\n")
