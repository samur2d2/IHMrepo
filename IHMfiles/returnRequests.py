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

def Centralizar(win):
    win.update_idletasks()

    width = win.winfo_width()
    frm_width = win.winfo_rootx() - win.winfo_x()
    win_width = width + 2 * frm_width

    height = win.winfo_height()
    titlebar_height = win.winfo_rooty() - win.winfo_y()
    win_height = height + titlebar_height + frm_width

    x = win.winfo_screenwidth() // 2 - win_width // 2
    y = win.winfo_screenheight() // 2 - win_height // 2

    win.geometry('{}x{}+{}+{}'.format(width, height, x, y-25))

    win.deiconify()