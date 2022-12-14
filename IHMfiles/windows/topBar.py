def CreatTopBar(master):
    from tkinter import Frame, Listbox, Scrollbar, Button
    from returnRequests import Centralizar, getTime
    from windows.alamsWindow import OpenAlarmsWindow
    from time import sleep
    import threading

    topFrame = Frame(master, width=1080, height=90, bg="#2E2E2E")
    topFrame.pack()   

    listbox = Listbox(topFrame, width=125, height=5, bg="#3C3C3C", fg="red", font=("Calibri", 11, "bold")) 
    listbox.place(x=90, y=3) 
    scrollbar = Scrollbar(topFrame)
    listbox.config(yscrollcommand = scrollbar.set) 
    scrollbar.config(command = listbox.yview) 

    def selected():
        for i in listbox.curselection():
            listbox.delete(i)

    buttonAlarms = Button(topFrame, text="Reconhecer", font=("Calibri", 12), width=10, height=1)
    buttonAlarms.configure(command=selected)
    buttonAlarms.place(x=980,y=10)

    buttonAlarms = Button(topFrame, text="Audit", font=("Calibri", 12), width=10, height=1)
    buttonAlarms.configure(command=lambda: OpenAlarmsWindow(master, Centralizar, topFrame), state="disabled")
    buttonAlarms.place(x=980,y=50)

    def alarme():
        cont=0
        while True:
            sleep(3)
            day, hour = getTime()
            textAlarm = day+ " - " +hour+ "......................ALARME " +str(cont)+ ".................FALHA NO EQUIPAMENTO " +str(cont)+ "................."
            with open("./IHMfiles/windows/files.txt", "r") as fonte:
                dados = fonte.read()
                if dados == "":
                    with open("./IHMfiles/windows/files.txt", "w") as fonte:
                        fonte.write(str(textAlarm))
                else:
                    with open("./IHMfiles/windows/files.txt", "a") as fonte:
                        fonte.write("\n" +str(textAlarm))
            listbox.insert(0, textAlarm)
            cont=cont+1

    # threading.Thread(target=alarme).start()