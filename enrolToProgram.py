import requests
import json
import hashlib


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
def enrolToProgram(url, pid, userid, timestart=None, periodtype=None, timeend=None):
    idsession = open_session(url)
    with open('keys.txt') as file:
        secret = file.readlines()[1].rstrip("\n")
        action = enrolToProgram.__name__
    form = f"{secret}{action}{idsession}"
    salt = hashlib.md5(form.encode('utf-8')).hexdigest()
    params = {"action": action, "salt": salt, "pid": pid, "userid": userid}
    if timestart is not None:
        params["timestart"] = timestart
    if periodtype is not None:
        params["periodtype"] = periodtype
    if timeend is not None:
        params["timeend"] = timeend
    response = requests.get(url+"/local/api/run.php", params)
    print(json.loads(response.text))


if __name__ == '__main__':
    enrolToProgram('https://sdo.ippss.ru', 14852, 276805)
