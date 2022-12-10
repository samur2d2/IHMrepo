import IHMfiles.returnRequests as Request
listaItens, listaHora, listaInput, listaSetpoint = [], [], [], []
definedRange = 4

#------------- LÊ O IP DO EQUIPAMENTO SELECIONADO NA IHM --------------------
#------------- VERIFICA SE O DIRETORIO DESTE IP EXISTE, SE NÃO ELE É CRIADO --------------------
with open("./IHMfiles/fileIP.txt", 'r') as fonte:
    IpOnFile = fonte.read()
    folder = Request.VerifyDir(IpOnFile)

#------------- CRIA AS VARIÁVEIS PARA ABRIR OS ARQUIVOS COM OS DADOS ATUAIS --------------------
day, hour = Request.getTime()
lerDados = folder[0:]+ "/input_" +day+ ".txt"
dadosLast = folder[0:]+ "/LASTinput_" +day+ ".txt"

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
    listaHora.append(hora)
    listaInput.append(input)
    listaSetpoint.append(setpoint)
print(listaHora)