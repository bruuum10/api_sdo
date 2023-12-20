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


# выполнение операции
# Если не переданы даты, то происходит выборка квитанций за последние 24 часа.
def getKvitancia(url, startdate=None, enddate=None):
    idsession = open_session(url)
    with open('keys.txt') as file:
        secret = file.readlines()[1].rstrip("\n")
        action = getKvitancia.__name__
    form = f"{secret}{action}{idsession}"
    salt = hashlib.md5(form.encode('utf-8')).hexdigest()
    params = {"action": action, "salt": salt}
    if startdate is not None:
        params["startdate"] = startdate
    if enddate is not None:
        params["enddate"] = enddate
    response = requests.get(url+"/local/api/run.php", params)
    inf = json.loads(response.text, object_pairs_hook=OrderedDict)
    pprint.pprint(inf)


if __name__ == '__main__':
    getKvitancia('https://sdo.pentaschool.ru', 1686517200, 1688418000)