import requests
import json
import hashlib



# отписка студента от программы

def unenrolToProgram(url, userid, pid):
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
    unenrolToProgram('https://sdo.vgaps.ru', 696049, 12)
    unenrolToProgram('https://sdo.urgaps.ru', 696049, 262)