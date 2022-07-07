maior = 0
menor = 0 
while True:
    peso = float(input('digite o seu peso')) #estrutura de repetiçao
    if peso == 1: #caso seja a primeira pessoa usar este codigo
            maior = peso
            menor = peso
    else: #caso não seja, usar esse outro codigo para verificar
        pass
    if peso > maior:
        maior = peso
    if peso < menor:
        menor = peso
    if peso == 0000: #conDção de parada
        break 
print(f' o amior peso foi de {maior} e o menor peso foi de {menor}')