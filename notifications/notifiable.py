from abc import ABC, abstractmethod

NOTIFIER_TG = "tg"


def make_notifier(notifier: str):
    if notifier == NOTIFIER_TG:
        from .telegram_notifier import TelegramNotifier
        return TelegramNotifier()
    else:
        raise ValueError(f'unknown notifier {notifier}')


class Message:
    images: []
    weather: str
    sentence: str

    def __init__(self, images: [], weather: str, sentence: str):
        self.images = images
        self.weather = weather
        self.sentence = sentence


class Notifiable(ABC):
    @abstractmethod
    def notify(self, message: Message):
        pass
