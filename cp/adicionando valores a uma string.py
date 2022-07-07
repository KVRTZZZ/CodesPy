lista1 = []
cont = 0
while True:
    print('digite valores para ser adicionado a uma lista')
    num = int(input(''))
    cont += 1
    if num not in lista1:
        lista1.append(num)
    else:
       print('numero já adicionado, irei desconsidera-lo')
    q = str(input('deseja continuar ?'))
    if q in 'Nn':
        break
print(f'você digitou {cont} valores, e  o maior valor de sua lista foi {max(lista1)}, e o menor foi {min(lista1)}')
lista1.sort()
print(lista1)