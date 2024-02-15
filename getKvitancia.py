import requests
import json
import pprint
import hashlib
from collections import OrderedDict
import config
from dotenv import load_dotenv
import os
from open_session import open_session

# Если не переданы даты, то происходит выборка квитанций за последние 24 часа.
def getKvitancia(org, startdate=None, enddate=None):
    url = config.getOrgsFromShortName(org)
    idsession = open_session(url)  # открытие сессии
    load_dotenv()
    secret = os.getenv("secret")
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
    getKvitancia('vgaps', 1686517200, 1688418000)