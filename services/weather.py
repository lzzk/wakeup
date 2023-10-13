import pyweathercn

# see https://github.com/BennyThink/pyweathercn for more info, thanks @BennyThink


def get_weather(city: str):
    w = pyweathercn.Weather(city)
    first_day = w.data['forecast'][0]

    # 重庆 星期五 小雨 19/15℃ 东北风3-4级
    return "{} {} {} {} {}".format(
        w.data['city'], first_day['date'], first_day['type'], first_day['temp'], first_day['wind'],
    )
