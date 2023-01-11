from tkinter import *

def create():
    root = Tk()       
    def changeOnHover(button, colorOnHover, colorOnLeave): 
        button.bind("<Enter>", func=lambda e: button.config(background=colorOnHover)) 

        button.bind("<Leave>", func=lambda e: button.config(background=colorOnLeave)) 

    navigatorFrame = Frame(root, width=1080, height=25, bg="lightgrey")
    navigatorFrame.pack()    
    bodyFrame = Frame(root, width=1080, height=525, bg="grey")
    bodyFrame.pack()   

    photo=PhotoImage(file="./images/valves/valvula-def.png")

    boton = Button(bodyFrame, border=0, image=photo, bg="grey")
    boton.place(x=60,y=100)

    changeOnHover(boton, "white", "grey") 

    root.mainloop()
create()