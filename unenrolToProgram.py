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


# отписка студента от программы

def unenrolToProgram(url, pid, userid):
    idsession = open_session(url)
    with open('keys.txt') as file:
        secret = file.readlines()[1].rstrip("\n")
        action = unenrolToProgram.__name__
    form = f"{secret}{action}{idsession}"
    salt = hashlib.md5(form.encode('utf-8')).hexdigest()
    params = {"action": action, "salt": salt, "pid": pid, "userid": userid}
    response = requests.get(url+"/local/api/run.php", params)
    print(json.loads(response.text))

if __name__ == '__main__':
    unenrolToProgram('https://sdo.niidpo.ru', 696049, 1281)
    unenrolToProgram('https://sdo.mcdo.moscow', 696049, 2169)