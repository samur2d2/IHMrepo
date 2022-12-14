#===================================================================== DEFINE OS IMPORTS UTILIZADOS
import tkinter as ttk
from windows.homeWindow import CreateHomeWindow
from windows.createObjects import importImages
#  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  - 

#===================================================================== DEFINE A CLASSE E O TAMANHO DA JANELA
master=ttk.Tk()
#  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  - 

#===================================================================== IMPORTA AS IMAGENS USADAS NOS BOTOES
listImages = importImages()
#  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  - 

#===================================================================== CRIA A TELA INICIAL
CreateHomeWindow(master, listImages)
#  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  - 

#===================================================================== INICIA O LOOP DA APLICACAO
master.mainloop()
#  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  - 