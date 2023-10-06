import argparse

import telebot
from BingImageCreator import ImageGen

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("tg_token", help="tg token")
    parser.add_argument("bing_cookie_U", help="bing cookie for U")
    parser.add_argument("bing_cookie_KievRPSSecAuth", help="bing cookie for KievRPSSecAuth")
    options = parser.parse_args()
    bot = telebot.TeleBot(options.tg_token)
    bing_cookie_u = options.bing_cookie_U
    bing_cookie_kiev = options.bing_cookie_KievRPSSecAuth

    def reply_dalle_image(message):
        start_words = "prompt:"
        if not message.text.startswith(start_words):
            return
        print("prompt" + message.text, "from user", message.from_user.id)

        s = message.text[len(start_words):].strip()

        all_cookies = []
        if bing_cookie_kiev:
            print("using kiev cookie")
            all_cookies = [{"name": "KievRPSSecAuth", "value": bing_cookie_kiev}]

        i = ImageGen(auth_cookie=bing_cookie_u, all_cookies=all_cookies)

        bot.reply_to(message, "Using bing DALL-E 3 generating images please wait")

        try:
            images = i.get_images(s)
        except Exception as e:
            print("error getting images", e)
            bot.reply_to(message, "Error getting images" + str(e))
            return

        print("got images", len(images))

        # download images and send them to telegram
        media = []
        for image in images:
            print("downloading image...", image)

            response = i.session.get(image)
            if response.status_code != 200:
                print("error downloading image", image, response.status_code)
                continue
            f = response.content
            media += [telebot.types.InputMediaPhoto(f)]
        bot.send_media_group(message.chat.id, media, reply_to_message_id=message.message_id)
        print("done")
        return

    @bot.message_handler(func=reply_dalle_image)
    def handle(message):
        pass

    def main():
        print("starting bot")
        bot.infinity_polling()


    main()
