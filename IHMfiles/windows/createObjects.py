from windows.baseColors import bodyBGcolor, navigatorBGcolor, mouseHoverColor
from tkinter import PhotoImage, Button
from PIL import ImageTk

def createObjects(Button, root):
    photo=ImageTk.PhotoImage(file= "./images/valves/valvula-def.png")

    boton = Button(root, border=0)
    boton.config(image=photo)
    boton.config(bg=bodyBGcolor())
    boton.place(x=60,y=100)

    return boton

def CreateNavigatorButtons(navigatorFrame, text, x, y=0, color="#686868", fontColor="white"):
    genericButton = Button(navigatorFrame, text=text, bg=color, fg=fontColor)
    genericButton.place(x=x,y=y)
    return genericButton

def changeOnHover(button, colorOnHover, colorOnLeave): 
    button.bind("<Enter>", func=lambda e: button.config(background=colorOnHover)) 
    button.bind("<Leave>", func=lambda e: button.config(background=colorOnLeave))

def CreateBodyButtons(bodyFrame, x, y, image, color="#686868"):
    genericButton = Button(bodyFrame, border=0, image=image, bg=color)
    genericButton.place(x=x,y=y)
    changeOnHover(genericButton, "white", color)
    return genericButton

def importImages():
    listImages = {}
    #--------------------BALANÇAS----------------------
    listImages['balanca_interlok_g'] = PhotoImage(file="./images/balance/balanca-interlok-g.png")
    listImages['balanca_ausent_g'] = PhotoImage(file="./images/balance/balanca-ausent-g.png")
    listImages['balanca_ppp_g'] = PhotoImage(file="./images/balance/balanca-ppp-g.png")
    listImages['balanca_run_g'] = PhotoImage(file="./images/balance/balanca-run-g.png")
    listImages['balanca_def_g'] = PhotoImage(file="./images/balance/balanca-def-g.png")
    listImages['balanca_interlok_m'] = PhotoImage(file="./images/balance/balanca-interlok-m.png")
    listImages['balanca_ausent_m'] = PhotoImage(file="./images/balance/balanca-ausent-m.png")
    listImages['balanca_ppp_m'] = PhotoImage(file="./images/balance/balanca-ppp-m.png")
    listImages['balanca_run_m'] = PhotoImage(file="./images/balance/balanca-run-m.png")
    listImages['balanca_def_m'] = PhotoImage(file="./images/balance/balanca-def-m.png")
    listImages['balanca_interlok_p'] = PhotoImage(file="./images/balance/balanca-interlok-p.png")
    listImages['balanca_ausent_p'] = PhotoImage(file="./images/balance/balanca-ausent-p.png")
    listImages['balanca_ppp_p'] = PhotoImage(file="./images/balance/balanca-ppp-p.png")
    listImages['balanca_run_p'] = PhotoImage(file="./images/balance/balanca-run-p.png")
    listImages['balanca_def_p'] = PhotoImage(file="./images/balance/balanca-def-p.png")
    #--------------------AQUECEDORES----------------------
    listImages['aquecedor_interlok_g'] = PhotoImage(file="./images/heater/aquecedor-interlok-g.png")
    listImages['aquecedor_ausent_g'] = PhotoImage(file="./images/heater/aquecedor-ausent-g.png")
    listImages['aquecedor_ppp_g'] = PhotoImage(file="./images/heater/aquecedor-ppp-g.png")
    listImages['aquecedor_run_g'] = PhotoImage(file="./images/heater/aquecedor-run-g.png")
    listImages['aquecedor_def_g'] = PhotoImage(file="./images/heater/aquecedor-def-g.png")
    listImages['aquecedor_interlok_m'] = PhotoImage(file="./images/heater/aquecedor-interlok-m.png")
    listImages['aquecedor_ausent_m'] = PhotoImage(file="./images/heater/aquecedor-ausent-m.png")
    listImages['aquecedor_ppp_m'] = PhotoImage(file="./images/heater/aquecedor-ppp-m.png")
    listImages['aquecedor_run_m'] = PhotoImage(file="./images/heater/aquecedor-run-m.png")
    listImages['aquecedor_def_m'] = PhotoImage(file="./images/heater/aquecedor-def-m.png")
    listImages['aquecedor_interlok_p'] = PhotoImage(file="./images/heater/aquecedor-interlok-p.png")
    listImages['aquecedor_ausent_p'] = PhotoImage(file="./images/heater/aquecedor-ausent-p.png")
    listImages['aquecedor_ppp_p'] = PhotoImage(file="./images/heater/aquecedor-ppp-p.png")
    listImages['aquecedor_run_p'] = PhotoImage(file="./images/heater/aquecedor-run-p.png")
    listImages['aquecedor_def_p'] = PhotoImage(file="./images/heater/aquecedor-def-p.png")
    #--------------------MOTORES----------------------
    listImages['motor_interlok_g'] = PhotoImage(file="./images/motors/motor-interlok-g.png")
    listImages['motor_ausent_g'] = PhotoImage(file="./images/motors/motor-ausent-g.png")
    listImages['motor_ppp_g'] = PhotoImage(file="./images/motors/motor-ppp-g.png")
    listImages['motor_run_g'] = PhotoImage(file="./images/motors/motor-run-g.png")
    listImages['motor_def_g'] = PhotoImage(file="./images/motors/motor-def-g.png")
    listImages['motor_interlok_m'] = PhotoImage(file="./images/motors/motor-interlok-m.png")
    listImages['motor_ausent_m'] = PhotoImage(file="./images/motors/motor-ausent-m.png")
    listImages['motor_ppp_m'] = PhotoImage(file="./images/motors/motor-ppp-m.png")
    listImages['motor_run_m'] = PhotoImage(file="./images/motors/motor-run-m.png")
    listImages['motor_def_m'] = PhotoImage(file="./images/motors/motor-def-m.png")
    listImages['motor_interlok_p'] = PhotoImage(file="./images/motors/motor-interlok-p.png")
    listImages['motor_ausent_p'] = PhotoImage(file="./images/motors/motor-ausent-p.png")
    listImages['motor_ppp_p'] = PhotoImage(file="./images/motors/motor-ppp-p.png")
    listImages['motor_run_p'] = PhotoImage(file="./images/motors/motor-run-p.png")
    listImages['motor_def_p'] = PhotoImage(file="./images/motors/motor-def-p.png")
    #--------------------SILO----------------------
    listImages['silo_0'] = PhotoImage(file="./images/silo/silo-0.png")
    listImages['silo_20'] = PhotoImage(file="./images/silo/silo-20.png")
    listImages['silo_40'] = PhotoImage(file="./images/silo/silo-40.png")
    listImages['silo_60'] = PhotoImage(file="./images/silo/silo-60.png")
    listImages['silo_80'] = PhotoImage(file="./images/silo/silo-80.png")
    listImages['silo_100'] = PhotoImage(file="./images/silo/silo-100.png")
    #--------------------VALVULAS----------------------
    listImages['valvula_interlok_g'] = PhotoImage(file="./images/valves/valvula-interlok-g.png")
    listImages['valvula_ausent_g'] = PhotoImage(file="./images/valves/valvula-ausent-g.png")
    listImages['valvula_ppp_g'] = PhotoImage(file="./images/valves/valvula-ppp-g.png")
    listImages['valvula_def_g'] = PhotoImage(file="./images/valves/valvula-def-g.png")
    listImages['valvula_run_g'] = PhotoImage(file="./images/valves/valvula-run-g.png")
    listImages['valvula_interlok_m'] = PhotoImage(file="./images/valves/valvula-interlok-m.png")
    listImages['valvula_ausent_m'] = PhotoImage(file="./images/valves/valvula-ausent-m.png")
    listImages['valvula_ppp_m'] = PhotoImage(file="./images/valves/valvula-ppp-m.png")
    listImages['valvula_def_m'] = PhotoImage(file="./images/valves/valvula-def-m.png")
    listImages['valvula_run_m'] = PhotoImage(file="./images/valves/valvula-run-m.png")
    listImages['valvula_interlok_p'] = PhotoImage(file="./images/valves/valvula-interlok-p.png")
    listImages['valvula_ausent_p'] = PhotoImage(file="./images/valves/valvula-ausent-p.png")
    listImages['valvula_ppp_p'] = PhotoImage(file="./images/valves/valvula-ppp-p.png")
    listImages['valvula_def_p'] = PhotoImage(file="./images/valves/valvula-def-p.png")
    listImages['valvula_run_p'] = PhotoImage(file="./images/valves/valvula-run-p.png")
    #--------------------BOMBAS----------------------
    listImages['bomba_interlok_g'] = PhotoImage(file="./images/waterpump/bomba-interlok-g.png")
    listImages['bomba_ausent_g'] = PhotoImage(file="./images/waterpump/bomba-ausent-g.png")
    listImages['bomba_ppp_g'] = PhotoImage(file="./images/waterpump/bomba-ppp-g.png")
    listImages['bomba_def_g'] = PhotoImage(file="./images/waterpump/bomba-def-g.png")
    listImages['bomba_run_g'] = PhotoImage(file="./images/waterpump/bomba-run-g.png")
    listImages['bomba_interlok_m'] = PhotoImage(file="./images/waterpump/bomba-interlok-m.png")
    listImages['bomba_ausent_m'] = PhotoImage(file="./images/waterpump/bomba-ausent-m.png")
    listImages['bomba_ppp_m'] = PhotoImage(file="./images/waterpump/bomba-ppp-m.png")
    listImages['bomba_def_m'] = PhotoImage(file="./images/waterpump/bomba-def-m.png")
    listImages['bomba_run_m'] = PhotoImage(file="./images/waterpump/bomba-run-m.png")
    listImages['bomba_interlok_p'] = PhotoImage(file="./images/waterpump/bomba-interlok-p.png")
    listImages['bomba_ausent_p'] = PhotoImage(file="./images/waterpump/bomba-ausent-p.png")
    listImages['bomba_ppp_p'] = PhotoImage(file="./images/waterpump/bomba-ppp-p.png")
    listImages['bomba_def_p'] = PhotoImage(file="./images/waterpump/bomba-def-p.png")
    listImages['bomba_run_p'] = PhotoImage(file="./images/waterpump/bomba-run-p.png")


    return listImages