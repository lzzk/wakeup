from telebot import TeleBot, types
from .notifiable import Notifiable, Message
from environment import Environment


class TelegramNotifier(Notifiable):
    bot: TeleBot
    token: str
    chat_id: str

    def __init__(self):
        token = Environment.get_tg_token()
        chat_id = Environment.get_tg_chat_id()

        if not token or token == "":
            raise ValueError("TG_TOKEN env variable not set")
        if not chat_id or chat_id == "":
            raise ValueError("TG_CHAT_ID env variable not set")

        self.token = token
        self.chat_id = chat_id
        self.bot = TeleBot(token)

    def notify(self, message: Message):
        m = message.format()
        print("sending message to telegram", m)

        if not message.images:
            self.bot.send_message(self.chat_id, m)
            return

        # todo: Investigate is there are possible to send multiple images in one message with caption
        # media = [types.InputMediaPhoto(image, caption=message.sentence) for image in message.images]
        # self.bot.send_media_group(chat_id, media=media)

        self.bot.send_photo(self.chat_id, photo=message.images[0], caption=m)
