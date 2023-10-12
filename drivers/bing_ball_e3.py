import os

from BingImageCreator import ImageGen
from .driver import Driver

bing_cookie_u = os.getenv('BING_AUTH_TOKEN')
bing_cookie_kiev = os.getenv('BING_AUTH_TOKEN_KIEV')


class BingBallE3Driver(Driver):
    def __init__(self):
        if bing_cookie_u is None:
            raise ValueError("BING_AUTH_TOKEN env variable not set")
        pass

    def generate_images(self, text: str):
        print("bing_ball_e3 generate_image", text)

        # test
        if os.getenv("CITY") == "重庆":
            print("env city is set to chongqing")
        if os.getenv("BING_AUTH_TOKEN").startswith("19C8bP8mG47AToz7tSyIzVSAzM6D"):
            print("env bing auth token is set to 19C8bP8mG47AToz7tSyIzVSAzM6D")
        if os.getenv("TG_TOKEN").startswith("6558579527"):
            print("env TG_TOKEN is set to 6558579527")

        all_cookies = []
        if bing_cookie_kiev:
            print("using kiev cookie")
            all_cookies = [{"name": "KievRPSSecAuth", "value": bing_cookie_kiev}]

        i = ImageGen(auth_cookie=bing_cookie_u, all_cookies=all_cookies)
        try:
            images = i.get_images(text)
            datas = []
            for image in images:
                print("downloading image: ", image)
                response = i.session.get(image)
                if response.status_code != 200:
                    print("error downloading image", image, response.status_code)
                    continue
                datas.append(response.content)
            return datas
        except Exception as e:
            raise ValueError(f'error getting images {e}')
