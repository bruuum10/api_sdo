import requests
import json
import pprint
import hashlib
from collections import OrderedDict
import config
from dotenv import load_dotenv
import os
from open_session import open_session

# выполнение операции
# username - login
def getUser(org, email=None, username=None):
    url = config.getOrgsFromShortName(org)
    idsession = open_session(url)  # открытие сессии
    load_dotenv()
    secret = os.getenv("secret")
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
    getUser('ipp', 'lelechka19.94@mail.ru')