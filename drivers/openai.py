import openai
import requests

from .driver import Driver
from environment import Environment


class OpenAIDriver(Driver):
    def __init__(self):
        openai.api_type = Environment.get_openai_api_type()
        openai.api_base = Environment.get_openai_api_base()
        openai.api_version = Environment.get_openai_api_version()
        openai.api_key = Environment.get_openai_api_key()
        pass

    def generate_images(self, text: str):
        response = openai.Image.create(
            prompt=text,
            size='1024x1024',
            n=1,
        )

        print("generate image success, start downloading...")

        # only one image is generated
        r = requests.get(response['data'][0]['url'])
        if r.status_code != 200:
            raise ValueError(f'error generating image by openai, err: {r.text}')

        return [r.content]


