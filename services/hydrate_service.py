from .gushici import random_sentence
from .weather import get_weather


class HydrateService:
    @staticmethod
    def random_sentence():
        return random_sentence()

    @staticmethod
    def get_weather(city: str):
        return get_weather(city)
