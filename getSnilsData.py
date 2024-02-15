import requests
import json
import pprint
import hashlib
from collections import OrderedDict
import config
from dotenv import load_dotenv
import os
from open_session import open_session

# если нет userids, то происходит выборка всех пользователей, у которых заполнено поле снилс
def getSnilsData(org, userids=None):
    url = config.getOrgsFromShortName(org)
    idsession = open_session(url) #открытие сессии
    load_dotenv()
    secret = os.getenv("secret")
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
    getSnilsData('vgaps', "238211,624040")