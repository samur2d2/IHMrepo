def CreateProcess1Window(master, photo):
    from returnRequests import OpenWindowProcess1, OpenWindowProcess2, OpenWindowProcess3, OpenWindowProcess4, OpenWindowProcess5
    from windows.createObjects import changeOnHover, CreateNavigatorButtons, CreateBodyButtons
    from tkinter import Frame, Button, Label
#============================================================================================== DEFINICAO DOS FRAMES
    navigatorFrame = Frame(master, width=1080, height=25, bg="#ABABAB")
    navigatorFrame.pack()    
    bodyFrame = Frame(master, width=1080, height=525, bg="#686868")
    bodyFrame.pack()
#  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  - 


#============================================================================================== BOTORES DA JANELA DE NAVEGACAO
    buttonProcess1 = CreateNavigatorButtons(navigatorFrame, "Process 1", 10, color="#DCDBDB", fontColor="black")
    buttonProcess1.configure(command=lambda: OpenWindowProcess1(master, navigatorFrame, bodyFrame, photo))

    buttonProcess2 = CreateNavigatorButtons(navigatorFrame, "Process 2", 75)
    buttonProcess2.configure(command=lambda: OpenWindowProcess2(master, navigatorFrame, bodyFrame, photo))

    buttonProcess3 = CreateNavigatorButtons(navigatorFrame, "Process 3", 140)
    buttonProcess3.configure(command=lambda: OpenWindowProcess3(master, navigatorFrame, bodyFrame, photo))

    buttonProcess4 = CreateNavigatorButtons(navigatorFrame, "Process 4", 205)
    buttonProcess4.configure(command=lambda: OpenWindowProcess4(master, navigatorFrame, bodyFrame, photo))

    buttonProcess5 = CreateNavigatorButtons(navigatorFrame, "Process 5", 270)
    buttonProcess5.configure(command=lambda: OpenWindowProcess5(master, navigatorFrame, bodyFrame, photo))
#  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -


#============================================================================================== BOTORES DO ESCOPO DA TELA
    label = Label(bodyFrame, image=photo['silo_0'], border=0)
    label.place(x=200, y=200)

    motor = CreateBodyButtons(bodyFrame, 150, 150, photo['motor_run_p'])
    valvula = CreateBodyButtons(bodyFrame, 200, 300, photo['valvula_run_p'])
#  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -