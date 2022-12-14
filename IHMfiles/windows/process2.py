def CreateProcess2Window(master, photo):
    from returnRequests import OpenWindowProcess1, OpenWindowProcess2, OpenWindowProcess3, OpenWindowProcess4, OpenWindowProcess5
    from tkinter import Frame, Button, Label
#============================================================================================== DEFINICAO DOS FRAMES
    navigatorFrame = Frame(master, width=1080, height=25, bg="#ABABAB")
    navigatorFrame.pack()    
    bodyFrame = Frame(master, width=1080, height=525, bg="#686868")
    bodyFrame.pack()         
#  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -


#============================================================================================== BOTORES DA JANELA DE NAVEGACAO
    def CreateNavigatorButtons(text, x, y=0, color="#686868", fontColor="white"):
        genericButton = Button(navigatorFrame, text=text, bg=color, fg=fontColor)
        genericButton.place(x=x,y=y)
        return genericButton

    buttonProcess1 = CreateNavigatorButtons("Process 1", 10)
    buttonProcess1.configure(command=lambda: OpenWindowProcess1(master, navigatorFrame, bodyFrame, photo))

    buttonProcess2 = CreateNavigatorButtons("Process 2", 75, color="#DCDBDB", fontColor="black")
    buttonProcess2.configure(command=lambda: OpenWindowProcess2(master, navigatorFrame, bodyFrame, photo))

    buttonProcess3 = CreateNavigatorButtons("Process 3", 140)
    buttonProcess3.configure(command=lambda: OpenWindowProcess3(master, navigatorFrame, bodyFrame, photo))

    buttonProcess4 = CreateNavigatorButtons("Process 4", 205)
    buttonProcess4.configure(command=lambda: OpenWindowProcess4(master, navigatorFrame, bodyFrame, photo))

    buttonProcess5 = CreateNavigatorButtons("Process 5", 270)
    buttonProcess5.configure(command=lambda: OpenWindowProcess5(master, navigatorFrame, bodyFrame, photo))
#  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -


#============================================================================================== LABEL INDICADO QUE A JANELA NAO ESTA SENDO UTILIZADA
    label = Label(bodyFrame, text="EMPTY", font=("Calibri", 42))
    label.place(x=420, y=200)
#  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  