from tkinter import *
import threading
from time import sleep

root = Tk()
root.geometry("1000x800")
root.config(bg="#686868")
def create():
    def changeOnHover(button, colorOnHover, colorOnLeave): 
        button.bind("<Enter>", func=lambda e: button.config(background=colorOnHover)) 
        button.bind("<Leave>", func=lambda e: button.config(background=colorOnLeave))   
    
    silo0=PhotoImage(file="./images/silo/silo-0.png")
    silo20=PhotoImage(file="./images/silo/silo-20.png")
    silo40=PhotoImage(file="./images/silo/silo-40.png")
    silo60=PhotoImage(file="./images/silo/silo-60.png")
    silo80=PhotoImage(file="./images/silo/silo-80.png")
    silo100=PhotoImage(file="./images/silo/silo-100.png")

    def silo():
        cont=0
        abastece=True
        while True:
            sleep(1)
            if abastece == True:
                if cont == 0:
                    label.configure(image=silo20)
                elif cont == 20:
                    label.configure(image=silo40)
                elif cont == 40:
                    label.configure(image=silo60)
                elif cont == 60:
                    label.configure(image=silo80)
                elif cont == 80:
                    label.configure(image=silo100)
                    abastece = False
                cont=cont+20
            else:
                if cont == 100:
                    label.configure(image=silo80)
                elif cont == 80:
                    label.configure(image=silo60)
                elif cont == 60:
                    label.configure(image=silo40)
                elif cont == 40:
                    label.configure(image=silo20)
                elif cont == 20:
                    label.configure(image=silo0)
                    abastece = True
                cont=cont-20

    label = Label(root, image=silo0, border=0)
    label.place(x=30,y=30)

    can = Canvas(root,bg='red',width=50,height=50)
    can.pack()
    photo=PhotoImage(file="./images/valves/valvula-def.png")
    can.create_image(50,50,image=photo)
    boton = Button(root, border=0, image=photo, bg="#686868")
    boton.place(x=500,y=50)

    photo2=PhotoImage(file="./images/valves/valvula-run.png")
    boton = Button(root, border=0, image=photo2, bg="#686868")
    boton.place(x=500,y=150)


    changeOnHover(boton, "white", "#686868") 
    threading.Thread(target=silo).start()
    root.mainloop()
create()



