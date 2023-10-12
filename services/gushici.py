import requests

# see http://gushi.ci/ for more info, thanks @xenv
URL = 'https://v1.jinrishici.com/all.json'


def random_sentence():
    r = requests.get(URL)
    if r.status_code == 200:
        return r.json()['content']
    else:
        return ValueError(f'failed to get random sentence from {URL}, err: {r.text}')
