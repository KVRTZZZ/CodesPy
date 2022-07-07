cont = soma = 0
while True:
	q = int(input('digite um numero: (999 para parar)\n'))
	#cont+= 1 #sempre colocar o contador embaixo do if para desconsiderar o flag como um numero digitado
	if q == 999:
		break
	soma += q
	cont += 1 # este e o correto 
print('programa encerrado')
print('soma dos seus algarismos foram de',soma, '\nForam digitados', cont,'numeros')