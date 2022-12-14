from returnRequests import *
def CreateHomeWindow(master, photo):
#============================================================================================== DEFINICAO OS IMPORTS UTILIZADOS
    from tkinter import Frame, Listbox, Scrollbar, Button
    from windows.topBar import CreatTopBar
#  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  


#============================================================================================== DEFINICAO DOS FRAMES
    CreatTopBar(master)          
    navigatorFrame = Frame(master, width=1080, height=25, bg="#ABABAB")       # 550 - 25 = 525
    navigatorFrame.pack()    
    bodyFrame = Frame(master, width=1080, height=525, bg="#686868")           # 525 - 525 = 0
    bodyFrame.pack()      
#  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  - 


#============================================================================================== DEFINIÇÃO DOS BOTOES
    def CreatButtons(text, x, y):
        genericalBtn = Button(bodyFrame, text=text, font=("Calibri", 18))
        genericalBtn.place(x=x, y=y)
        return genericalBtn

    buttonProcess1 = CreatButtons("Process 1", 200, 100)
    buttonProcess1.configure(command=lambda: OpenWindowProcess1(master, navigatorFrame, bodyFrame, photo))

    buttonProcess2 = CreatButtons("Process 2", 200, 200)
    buttonProcess2.configure(command=lambda: OpenWindowProcess2(master, navigatorFrame, bodyFrame, photo))

    buttonProcess3 = CreatButtons("Process 3", 200, 300)
    buttonProcess3.configure(command=lambda: OpenWindowProcess3(master, navigatorFrame, bodyFrame, photo))

    buttonProcess4 = CreatButtons("Process 4", 350, 100)
    buttonProcess4.configure(command=lambda: OpenWindowProcess4(master, navigatorFrame, bodyFrame, photo))

    buttonProcess5 = CreatButtons("Process 5", 350, 200)
    buttonProcess5.configure(command=lambda: OpenWindowProcess5(master, navigatorFrame, bodyFrame, photo))
    
#  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  