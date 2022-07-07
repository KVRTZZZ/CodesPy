termo = int(input('digite o primeiro termo de uma razao: '))
razao = int(input('digite uma razao para sua P.A: '))
decimo = termo + 10 * razao
for c in range (termo, decimo, razao):
	print(c, end=' > ')
print('ACABOU')