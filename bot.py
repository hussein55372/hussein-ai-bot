import os
from flask import Flask, request
from telegram import Update, Bot
from telegram.ext import Dispatcher, CommandHandler
import logging

app = Flask(__name__)

BOT_TOKEN = os.environ.get("BOT_TOKEN")
bot = Bot(token=BOT_TOKEN)

@app.route('/')
def home():
    return "بوت حسين شغال 💙"

def start(update: Update, context):
    update.message.reply_text("هلا حبي حسين 😍 البوت اشتغل!")

@app.route(f"/{BOT_TOKEN}", methods=["POST"])
def telegram_webhook():
    update = Update.de_json(request.get_json(force=True), bot)
    dispatcher = Dispatcher(bot, None, workers=0)
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.process_update(update)
    return "ok"

if __name__ == "__main__":
    app.run(debug=True)
