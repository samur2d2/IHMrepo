import matplotlib.pyplot as plotter
from matplotlib.animation import FuncAnimation
import returnRequests as Request

definedRange = 6

def Grafico():
#------------- LÊ O IP DO EQUIPAMENTO SELECIONADO NA IHM --------------------
#------------- VERIFICA SE O DIRETORIO DESTE IP EXISTE, SE NÃO ELE É CRIADO --------------------
    with open("./IHMfiles/fileIP.txt", 'r') as fonte:
        IpOnFile = fonte.read()
        folder = Request.VerifyDir(IpOnFile)

#------------- CRIA AS VARIÁVEIS PARA ABRIR OS ARQUIVOS COM OS DADOS ATUAIS --------------------
    day, hour = Request.getTime()
    lerDados = folder[0:]+ "/input_" +day+ ".txt"
#-----------------------------------------------------------------------------------------------

    fig, ax = plotter.subplots()
    fig.tight_layout()
    fig.subplots_adjust(bottom=0.25)
    fig.set_figheight(4)
    fig.set_figwidth(12)
    
    def animar(i):
        listaItens, xSET, ySET, xPID, yPID = [], [], [], [], []
#------------- LÊ TODOS OS DADOS DE UM TXT E SUBSTITUI A QUEBRA DE LINHA POR ESPAÇO --------------------
        with open(lerDados, 'r') as fonte:
            dadosFile = fonte.read()
        dadosFile = dadosFile.replace('\n', " ")

#------------- SEPARA AS STRINGS LIDAS A CADA " " EM UMA LISTA DE STRINGS E ORDENA DO MAIS RECENTE PRO MAIS ANTIGO --------------------
        for itens in dadosFile.split(" "):
            listaItens.append(itens)
        listaItens.reverse()

#------------- SEPARA OS ITENS ATÉ O LIMITE PRE DEFINIDO (definedRange) --------------------
        listaItens = listaItens[:definedRange]
#------------- SEPARA TODOS OS ITEMS EM 3 LISTAS DISTINTAS PARA CADA EIXO DO GRAFICO --------------------
        for item in listaItens:
            hora, input, setpoint = item.split(",")
            ySET.append(float(setpoint))
            xSET.append(hora)
            yPID.append(float(input))
            xPID.append(hora)
#--------------------------------------------------------------------------------------------------------

        ax.clear()
        ax.plot(xSET,ySET)
        ax.plot(xPID,yPID) 

        for tick in ax.get_xticklabels(): 
            tick.set_rotation(90)

    ani = FuncAnimation(fig, animar, interval = 1000)
    plotter.show()

Grafico()