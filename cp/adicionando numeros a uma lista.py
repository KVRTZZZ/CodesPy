lista = []
impares = []
pares= []
while True:
    q = int(input('digite um valor para ser adicionado a uma lista\n'))
    lista.append(q)
    if q in lista:
        if q % 2 == 0:
           pares.append(q)
        else:
            impares.append(q)
    sn = int(input('deseja continuar? [digite 0 para parar/ 1 para continuar]\n'))
    if sn == 0:
        break
print(f'foram digitados {len(lista)} valores')
print(f'os pares foram {pares} e os impares foram {impares}')