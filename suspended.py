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
# блокировка студентов
# значения параматра value:
# 0 – нет блокировок
# 1 – блокировка по причине финансовой задолженности, соответствует значению статуса в Слушателе "фин. задолженность"
# 3 – блокировка по причине академ. задолженности, соответствует значению статуса в Слушателе "академ. задолженность"
# 5 – блокировка по причине временной блокировки, соответствует значению статуса в Слушателе «Временная блокировка»
# 6 – блокировка по причине полного возврата Д/С, соответствует значению статуса в Слушателе «полный возврат д/с»
# если параметр value не передан, то он по уиолчанию принимается за 0

def suspended(url, userid, pid, value=None):
    idsession = open_session(url)
    with open('keys.txt') as file:
        secret = file.readlines()[1].rstrip("\n")
        action = suspended.__name__
    form = f"{secret}{action}{idsession}"
    salt = hashlib.md5(form.encode('utf-8')).hexdigest()
    params = {"action": action, "salt": salt,"userid": userid, "pid": pid }
    if value is not None:
        params["value"] = value
    response = requests.get(url+"/local/api/run.php", params)
    inf = response.text
    print(inf)


if __name__ == '__main__':
     # suspended('https://sdo.adpo-edu.ru', 696049, 4753, 3)
     suspended('https://sdo.adpo-edu.ru', 696733, 1568, 1)