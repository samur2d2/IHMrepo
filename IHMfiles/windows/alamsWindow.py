def OpenAlarmsWindow(master,Centralizar, topFrame):
    from tkinter import Toplevel, Listbox, Scrollbar
    alarmsWindow = Toplevel(master)
    alarmsWindow.title("Alarmes") 
    alarmsWindow.minsize(800, 600)
    Centralizar(alarmsWindow)

    listbox = Listbox(alarmsWindow, width=115, height=35, bg="#3C3C3C", fg="red", font=("Calibri", 11, "bold")) 
    listbox.pack() 
    scrollbar = Scrollbar(topFrame)
    listbox.config(yscrollcommand = scrollbar.set) 
    scrollbar.config(command = listbox.yview) 

    with open ("./IHMfiles/windows/files.txt", "r") as fonte:
        dados = fonte.read()
    dados = dados[1:]
    for item in dados.split("\n"):
        listbox.insert(0, item)