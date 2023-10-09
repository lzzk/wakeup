import os

from BingImageCreator import ImageGen
from telebot import TeleBot, types

token = os.getenv("TG_TOKEN")
webhook = os.getenv("TG_WEBHOOK")
bing_cookie_u = os.getenv('BING_AUTH_TOKEN')
bing_cookie_kiev = os.getenv('BING_AUTH_TOKEN_KIEV')

bot = TeleBot(token)

if webhook:
    bot.delete_webhook()
    bot.set_webhook(webhook)


@bot.message_handler(commands=['create', 'c'])
def generate_image(message):
    bot.reply_to(message, "Using bing DALL-E 3 generating images please wait...")
    s = message.text[len("/create"):].strip()
    if not s:
        bot.reply_to(message, "Please enter a prompt")
        return

    all_cookies = []
    if bing_cookie_kiev:
        print("using kiev cookie")
        all_cookies = [{"name": "KievRPSSecAuth", "value": bing_cookie_kiev}]

    i = ImageGen(auth_cookie=bing_cookie_u, all_cookies=all_cookies)
    try:
        images = i.get_images(s)
    except Exception as e:
        print("error getting images", e)
        bot.reply_to(message, "generating images failed "+str(e))
        return

    print("got images:", len(images))

    # download images and send them to telegram
    media = []
    for image in images:
        response = i.session.get(image)
        if response.status_code != 200:
            print("error downloading image", image, response.status_code)
            continue
        f = response.content
        media += [types.InputMediaPhoto(f)]
    bot.send_media_group(message.chat.id, media, reply_to_message_id=message.message_id)
    print("done")
    return


def telegram_handler(event):
    print("start handling telegram event in background...", event)
    bot.process_new_updates([types.Update.de_json(event)])
