lista = list()
while True:
	num = int(input('digite um valor para ser adicionado a lista: '))
	if num not in lista:
		lista.append(num)
		print('valor adicionado')
	else:
	 	print('numero ja inserido, irei descarta-lo')
	sn = str(input('voce quer continuar? \n'))
	if sn in 'nN':
	 	break
	elif sn in 'sS':
	   pass
	else:
	     print('digite somente sim ou nao')
	     rsn = str(input(''))
print('Fim')
print(lista)