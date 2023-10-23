from abc import ABC, abstractmethod

DRIVER_BING_DALLE3 = "bing_dalle3"
DRIVER_OPENAI = "openai"


class Driver(ABC):
    @abstractmethod
    def generate_images(self, text: str):
        pass


def make_image_driver(driver: str) -> Driver:
    if driver == DRIVER_BING_DALLE3:
        from .bing_dalle3 import BingDallE3Driver
        return BingDallE3Driver()
    elif driver == DRIVER_OPENAI:
        from .openai import OpenAIDriver
        return OpenAIDriver()
    else:
        raise ValueError(f'unknown driver {driver}')
