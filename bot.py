from dotenv import load_dotenv
import os
import requests
import telebot

load_dotenv()

TELEGRAM_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
ANTHROPIC_KEY = os.getenv("ANTHROPIC_API_KEY")

bot = telebot.TeleBot(TELEGRAM_TOKEN)

def ask_claude(question):
    response = requests.post(
        "https://api.anthropic.com/v1/messages",
        headers={
            "x-api-key": ANTHROPIC_KEY,
            "anthropic-version": "2023-06-01",
            "content-type": "application/json"
        },
        json={
            "model": "claude-haiku-4-5-20251001",
            "max_tokens": 300,
            "system": "You are Egor's personal assistant. Egor is busy. Be helpful, direct and brief on his behalf.",
            "messages": [
                {"role": "user", "content": question}
            ]
        }
    )
    data = response.json()
    return data["content"][0]["text"]

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    user_text = message.text
    response = ask_claude(user_text)
    bot.reply_to(message, response)

print("Bot is running...")
bot.polling()