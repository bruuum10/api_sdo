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
# если нет userids, то происходит выборка всех пользователей, у которых заполнено поле снилс
def getSnilsData(url, userids=None):
    idsession = open_session(url)
    with open('keys.txt') as file:
        secret = file.readlines()[1].rstrip("\n")
        action = getSnilsData.__name__
    form = f"{secret}{action}{idsession}"
    salt = hashlib.md5(form.encode('utf-8')).hexdigest()
    params = {"action": action, "salt": salt}
    if userids is not None:
        params["userids"] = userids
    response = requests.get(url+"/local/api/run.php", params)
    inf = json.loads(response.text, object_pairs_hook=OrderedDict)
    pprint.pprint(inf)


if __name__ == '__main__':
    getSnilsData('https://sdo.vgaps.ru', "238211,624040")