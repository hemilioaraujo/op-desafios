inicio = 1
fim = 1000000
palindromos = []

for i in range(inicio, fim + 1):
    textoA = str(i)
    textoB = textoA[::-1]
    if textoA == textoB:
        palindromos.append(i)

print(palindromos)
