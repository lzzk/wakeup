import os

from drivers import make_image_driver
from notifications import make_notifier, Message
from services import HydrateService

# DRIVER = "bing_ball_e3"
DRIVER = "openai"
CHANNELS = ["tg"]
CITY = os.getenv("CITY", "重庆")


if __name__ == '__main__':
    service = HydrateService()

    for channel in CHANNELS:
        sentence = service.random_sentence()
        images = make_image_driver(DRIVER).generate_images(sentence)
        m = Message(images, service.get_weather(CITY), sentence)

        make_notifier(channel).notify(m)

    print("done")

