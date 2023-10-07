import telebot
import os

from flask import Flask
from flask import request
from handlers.tg import register_tg_handlers

TOKEN = os.getenv('TG_TOKEN')

app = Flask(__name__, )
bot = telebot.TeleBot(token=TOKEN, threaded=False)

register_tg_handlers(bot)


@app.route("/")
def hello_world():
    return "Hello, World!"


@app.route('/tg_webhook', methods=['POST', 'GET'])
def webhook():
    update = telebot.types.Update.de_json(request.stream.read().decode("utf-8"))
    bot.process_new_updates([update])
    return "ok", 200


if __name__ == "__main__":
    app.run(debug=False, host='0.0.0.0', port=8088)
