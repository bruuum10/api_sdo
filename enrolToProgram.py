import requests
import hashlib
import config
from dotenv import load_dotenv
import os
from open_session import open_session

# запись студента на программу
# timestart и timeend дата и время в формате UNIXTIME (поля не обязательные).
# Если не передать timestart, то подставится текущее время
# Если не передать timeend, то дата и время будет расчитано исходя из длительности программы в настройках
# periodtype  – устанавливает тип обучения слушателя по программе. Нормативный (normal) или ускоренный (short).
# Если параметр periodtype не передается, то тип обучения берется из настроек УЦ
def enrolToProgram(org, userid, pid, timestart=None, timeend=None, periodtype=None):
    url = config.getOrgsFromShortName(org)
    idsession = open_session(url)  # открытие сессии
    load_dotenv()
    secret = os.getenv("secret")
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
    print(response.json())


if __name__ == '__main__':
    #enrolToProgram('https://sdo.ippss.ru', 441299, 14871, 1707253200, 1714683599)
    enrolToProgram('ipp', 441299, 14871, 1707426000, 1714856399)
    # enrolToProgram('https://sdo.vgaps.ru', 696733, 12)
    # enrolToProgram('https://sdo.urgaps.ru', 696733, 262)
    # enrolToProgram('https://sdo.niidpo.ru', 696733, 1281)
    # enrolToProgram('https://sdo.mcdo.moscow', 696733, 2169)
