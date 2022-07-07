lista = []
while True:
	num = int(input('digite um valor para ser adicionado a lista \n'))
	if num in lista:
		print('esse valor ja foi adicionado, vou desconsidera-lo')
	else:
	 	lista.append(num)
	 	sn = str(input('voce quer continuar? \n')).upper()
	if sn in 'Nn':
		break
	elif sn in 'Ss':
		print('continuando')
	else:
		print('digite somente sim ou nao')
		sn = str(input(''))
lista.sort()
print('Fim', lista)
        