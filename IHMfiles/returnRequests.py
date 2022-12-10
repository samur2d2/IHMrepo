import os
from datetime import datetime

def getTime():
    now = str(datetime.now())
    day, hour = now.split(" ")
    hourSent=hour[0: 8]
    day=day.replace("-", "_")
    return day, hourSent

def VerifyDir(IPSender):
    if (os.path.exists("./ArquivosHistorico/"+IPSender)) != True:
        os.makedirs("./ArquivosHistorico/"+IPSender)
    return "./ArquivosHistorico/"+IPSender