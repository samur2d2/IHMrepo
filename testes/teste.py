dados = "./ArquivosHistorico/192.168.0.10/input_2022_12_10.txt"
definedRange = 4
listaItens = []

#------------- LÊ TODOS OS DADOS DE UM TXT E SUBSTITUI A QUEBRA DE LINHA POR ESPAÇO --------------------
with open(dados, 'r') as fonte:
    dadosFile = fonte.read()
dadosFile = dadosFile.replace('\n', " ")

#------------- SEPARA AS STRINGS LIDAS A CADA " " EM UMA LISTA DE STRINGS E ORDENA DO MAIS RECENTE PRO MAIS ANTIGO --------------------
for itens in dadosFile.split(" "):
    listaItens.append(itens)
listaItens.reverse()

#------------- SEPARA OS ITENS ATÉ O LIMITE PRE DEFINIDO (definedRange) --------------------
listaItens = listaItens[:definedRange]
print(listaItens)