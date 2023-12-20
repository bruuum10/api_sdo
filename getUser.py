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
# username - login
def getUser(url, email=None, username=None):
    idsession = open_session(url)
    with open('keys.txt') as file:
        secret = file.readlines()[1].rstrip("\n")
        action = getUser.__name__
    form = f"{secret}{action}{idsession}"
    salt = hashlib.md5(form.encode('utf-8')).hexdigest()
    params = {"action": action, "salt": salt}
    if email is not None:
        params["email"] = email
    if username is not None:
        params["username"] = username
    response = requests.get(url+"/local/api/run.php", params)
    inf = json.loads(response.text, object_pairs_hook=OrderedDict)
    pprint.pprint(inf)


if __name__ == '__main__':
    getUser('https://sdo.ippss.ru', 'lelechka19.94@mail.ru')