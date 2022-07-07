lista = [[], []]
for c in range(1,8):
    q = int(input('digite um valor númerico: '))
    if q % 2 == 0:
       lista[0].append(q)
    else:
        lista[1].append(q)
print(f'os valores impares sao {lista[1]} e os pares são {lista[0]}')