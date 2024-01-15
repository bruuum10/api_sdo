import requests
import json
import pprint
import hashlib
from collections import OrderedDict


# открытие сессии
def open_session(url):
    action = "open"
    with open('keys.txt') as file:
        secret_open = file.readlines()[0].rstrip("\n")
    form = f"{secret_open}{action}"
    salt = hashlib.md5(form.encode('utf-8')).hexdigest()
    params = {"action": action, "salt": salt}
    response = requests.get(url+"/local/api/run.php", params)
    idsession = response.json()["transaction"]
    return idsession


# Передача отзывов на сайты.
# Ссылка, по которой получают отзывы отличается от той, по которой Слушатель их забирает
# date1 = начальная дата и date2 = конечная дата - необязательные параметры
# По умолчанию, если не переданы параметры date1 и date2, данные возвращаются за неделю
def getReviews(url, date1=None, date2=None):
    idsession = open_session(url)
    with open('keys.txt') as file:
        secret = file.readlines()[1].rstrip("\n")
        action = getReviews.__name__
    form = f"{secret}{action}{idsession}"
    salt = hashlib.md5(form.encode('utf-8')).hexdigest()
    params = {"action": action, "salt": salt}
    if date1 is not None:
        params["date1"] = date1
    if date2 is not None:
        params["date2"] = date2
    response = requests.get(url+"/local/api/review.php", params)
    inf = json.loads(response.text, object_pairs_hook=OrderedDict)
    pprint.pprint(inf)


if __name__ == '__main__':
     getReviews('https://sdo.ippss.ru')
    # getReviews('https://sdo.pentaschool.ru')
    #  getReviews('https://sdo.adpo-edu.ru')
    # getReviews('https://sdo.vgaps.ru')
    # getReviews('https://sdo.urgaps.ru')
    # getReviews('https://sdo.niidpo.ru')
    # getReviews('https://sdo.mcdo.moscow')
#   getReviews('https://sdo.ippss.ru', 1705237080, 1705323480)


