import os

from datetime import datetime
from telebot import TeleBot, types
from .notifiable import Notifiable, Message

token = os.getenv("TG_TOKEN")
chat_id = os.getenv("TG_CHAT_ID")


class TelegramNotifier(Notifiable):
    bot: TeleBot

    def __init__(self):
        if not token:
            raise ValueError("TG_TOKEN env variable not set")
        if not chat_id:
            raise ValueError("TG_CHAT_ID env variable not set")

        self.token = token
        self.bot = TeleBot(token)

    def notify(self, message: Message):
        if not message.images:
            return

        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        msg = "{}\n\n今日诗句: {}\n\n起床时间: {}".format(message.weather, message.sentence, now)

        # todo: Investigate is there are possible to send multiple images in one message with caption
        # media = [types.InputMediaPhoto(image, caption=message.sentence) for image in message.images]
        # self.bot.send_media_group(chat_id, media=media)

        self.bot.send_photo(chat_id, photo=message.images[0], caption=msg)
