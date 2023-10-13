import openai
import requests

from .driver import Driver

# Available env variables, see python openai package for more info
# OPENAI_API_BASE: https://api.openai.com/v1
# OPENAI_API_TYPE: open_ai
# OPENAI_API_VERSION: None
# OPENAI_API_KEY: None


class OpenAIDriver(Driver):
    def __init__(self):
        pass

    def generate_images(self, text: str):
        print("generate image using openai", text)

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


