import requests
import hashlib
import config
from dotenv import load_dotenv
import os
from open_session import open_session

# блокировка студентов
# значения параматра value:
# 0 – нет блокировок
# 1 – блокировка по причине финансовой задолженности, соответствует значению статуса в Слушателе "фин. задолженность"
# 3 – блокировка по причине академ. задолженности, соответствует значению статуса в Слушателе "академ. задолженность"
# 5 – блокировка по причине временной блокировки, соответствует значению статуса в Слушателе «Временная блокировка»
# 6 – блокировка по причине полного возврата Д/С, соответствует значению статуса в Слушателе «полный возврат д/с»
# если параметр value не передан, то он по уиолчанию принимается за 0

def suspended(org, userid, pid, value=None):
    url = config.getOrgsFromShortName(org)
    idsession = open_session(url)  # открытие сессии
    load_dotenv()
    secret = os.getenv("secret")
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
     suspended('adpo', 696049, 4753, 0)
