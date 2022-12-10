from tkinter import * 
from tkinter.ttk import *

master = Tk() 
master.geometry("720x480")
master.bind("<F11>", lambda event: master.attributes("-fullscreen", True))
master.bind("<Escape>", lambda event: master.attributes("-fullscreen", False))

def openNewWindowOne(): 
    newWindow = Toplevel(master) 
    newWindow.title("New Window One") 
    newWindow.geometry("200x200") 
    
    Label(newWindow, text ="This is a one").pack() 
  
def openNewWindowTwo(): 
    newWindow = Toplevel(master) 
    newWindow.title("New Window Two") 
    newWindow.geometry("200x200") 
    
    Label(newWindow, text ="This is a two").pack() 

btn = Button(master, text ="Click to open window one", command = openNewWindowOne).pack(pady = 10) 
btn = Button(master, text ="Click to open window two", command = openNewWindowTwo).pack(pady = 20) 



mainloop() 