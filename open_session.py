import requests
import hashlib
from dotenv import load_dotenv
import os

#открытие сессии
def open_session(url):
    action = "open"
    load_dotenv()
    secret_open = os.getenv("secret_open")
    form = f"{secret_open}{action}"
    salt = hashlib.md5(form.encode('utf-8')).hexdigest()
    params = {"action": action, "salt": salt}
    response = requests.get(url+"/local/api/run.php", params)
    idsession = response.json()["transaction"]
    return idsession