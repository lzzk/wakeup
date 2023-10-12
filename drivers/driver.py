from abc import ABC, abstractmethod

DRIVER_BING_BALL_E3 = "bing_ball_e3"
DRIVER_BAIDU = "baidu"


class Driver(ABC):
    @abstractmethod
    def generate_images(self, text: str):
        pass


def make_image_driver(driver: str) -> Driver:
    if driver == DRIVER_BING_BALL_E3:
        from .bing_ball_e3 import BingBallE3Driver
        return BingBallE3Driver()
    else:
        raise ValueError(f'unknown driver {driver}')