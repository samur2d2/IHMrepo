from datetime import datetime
import socket
import os

from windows.process1 import CreateProcess1Window
from windows.process2 import CreateProcess2Window
from windows.process3 import CreateProcess3Window
from windows.process4 import CreateProcess4Window
from windows.process5 import CreateProcess5Window

def getIP():
    st = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:       
        st.connect(('10.255.255.255', 1))
        IP = st.getsockname()[0]
    except Exception:
        IP = '127.0.0.1'
    finally:
        st.close()
    return IP

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

def SaveSetpoint(ip, eventDay, eventHour, eventType, eventValue):
    folder = VerifyDir(ip)
    file = folder+"/setpoint_" +eventDay+ ".txt"
    fileLast = folder+"/LAST"+eventType+"_"+eventDay+".txt"
    try:
        with open(fileLast, 'r+') as fonte:
            lastMinute = fonte.read()[3:5]
    except:
        open(fileLast, 'w')
    try:
        with open(file, 'r+') as fonte:
            data = fonte.read()
            if data == "":
                fonte.write(eventHour+","+eventValue+";")
            elif eventHour[6:8] == "00" or lastMinute != eventHour[3:5]:
                fonte.write("\n"+eventHour+","+eventValue+";")
            else:
                fonte.write(" "+eventHour+","+eventValue+";")
    except:
        open(file, 'w')

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


def explodeHomeWindow(navigatorFrame, bodyFrame):
    navigatorFrame.destroy()
    bodyFrame.destroy()

def OpenWindowProcess1(master, navigatorFrame, bodyFrame, photo):
    explodeHomeWindow(navigatorFrame, bodyFrame)
    CreateProcess1Window(master, photo)

def OpenWindowProcess2(master, navigatorFrame, bodyFrame, photo):
    explodeHomeWindow(navigatorFrame, bodyFrame)
    CreateProcess2Window(master, photo)

def OpenWindowProcess3(master, navigatorFrame, bodyFrame, photo):
    explodeHomeWindow(navigatorFrame, bodyFrame)
    CreateProcess3Window(master, photo)

def OpenWindowProcess4(master, navigatorFrame, bodyFrame, photo):
    explodeHomeWindow(navigatorFrame, bodyFrame)
    CreateProcess4Window(master, photo)

def OpenWindowProcess5(master, navigatorFrame, bodyFrame, photo):
    explodeHomeWindow(navigatorFrame, bodyFrame)
    CreateProcess5Window(master, photo)