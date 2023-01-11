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
    posx,posy=50,50
    tubo1 = CreateBodyButtons(bodyFrame, Label, posx+68, posy+192, photo['tubo_joelho_no_p'])
    silo1 = CreateBodyButtons(bodyFrame, Label, posx, posy, photo['silo_0'])
    tubo1 = CreateBodyButtons(bodyFrame, Label, posx+93, posy+206, photo['tubo_fim_oeste_p'])
    valvula1 = CreateBodyButtons(bodyFrame, Button, posx+117, posy+180, photo['horz_valvula_run_p'])
    tubo1 = CreateBodyButtons(bodyFrame, Label, posx+168, posy+206, photo['tubo_fim_leste_p'])
    tubo1 = CreateBodyButtons(bodyFrame, Label, posx+190, posy+206, photo['tubo_joelho_ls_p'])
    tubo1 = CreateBodyButtons(bodyFrame, Label, posx+203, posy+230, photo['tubo_fim_sul_p'])

    posx, posy = posx+100, posy+250
    motor = CreateBodyButtons(bodyFrame, Button, posx, posy, photo['horz_oeste_motor_run_p'])
    tubo3 = CreateBodyButtons(bodyFrame, Label, posx+47, posy+15, photo['correia_run_3_p'])

    posx,posy=800,45
    moinho1 = CreateBodyButtons(bodyFrame, Label, posx, posy, photo['tanque_100_g'])
    tubo1 = CreateBodyButtons(bodyFrame, Label, posx-20, posy+150, photo['tubo_joelho_os_p'])
    tubo1 = CreateBodyButtons(bodyFrame, Label, posx-20, posy+170, photo['tubo_vert_pp'])
    tubo1 = CreateBodyButtons(bodyFrame, Label, posx-28, posy+200, photo['tubo_joelho_nl_p'])
    tubo1 = CreateBodyButtons(bodyFrame, Label, posx-106, posy+208, photo['tubo_horz_p'])
    valvula1 = CreateBodyButtons(bodyFrame, Button, posx-150, posy+182, photo['horz_valvula_run_p'])
    tubo1 = CreateBodyButtons(bodyFrame, Label, posx-260, posy+188, photo['tubo_horz_p'])
    tubo1 = CreateBodyButtons(bodyFrame, Label, posx-280, posy+188, photo['tubo_joelho_os_p'])
    tubo1 = CreateBodyButtons(bodyFrame, Label, posx-280, posy+208, photo['tubo_vert_p'])
    
    # tubo1 = CreateBodyButtons(bodyFrame, Label, posx-150, posy+188, photo['tubo_joelho_os_p'])
    # tubo1 = CreateBodyButtons(bodyFrame, Label, posx-150, posy+213, photo['tubo_fim_sul_p'])   

    posx,posy=500,400
    tubo1 = CreateBodyButtons(bodyFrame, Label, posx, posy, photo['moinho_ausent_p'])   
#  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -