numeros = list()
while True:
    n = int(input('digite um valor: '))
    if n not in numeros:
        numeros.append(n)
        print('valor adicionado: ')
    else:
        print('valor duplicado')
    r = str(input('quer continuar?: '))
    if r in 'Nn':
        break
print(numeros)