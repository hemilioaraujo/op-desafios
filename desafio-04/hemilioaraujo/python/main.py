def tabuleiro():
    entrada = []
    for i in range(8):
        linha = []
        for x in range(8):
            linha.append(int(input('Entre com valor [%i][%i]:'%(i,x))))
        entrada.append(linha)
    return entrada

peao, bispo, cavalo, torre, rainha, rei = 0,0,0,0,0,0

mesa = tabuleiro()

print()

print('Você adicionou este tabuleiro: \n')

for linha in range(8):
    print(mesa[linha])

for linha in range(8):
    peao += mesa[linha].count(1)
    bispo += mesa[linha].count(2)
    cavalo += mesa[linha].count(3)
    torre += mesa[linha].count(4)
    rainha += mesa[linha].count(5)
    rei += mesa[linha].count(6)

texto ='''
Peão: {} peça(s)
Bispo: {} peça(s)
Cavalo: {} peça(s)
Torre: {} peça(s)
Rainha: {} peça(s)
Rei: {} peça(s)
'''

print(texto.format(peao,bispo,cavalo,torre,rainha,rei))
    
