import pyweathercn

# see https://github.com/BennyThink/pyweathercn for more info, thanks @BennyThink


def get_weather(city: str):
    w = pyweathercn.Weather(city)

    return "{}".format(w.today())
