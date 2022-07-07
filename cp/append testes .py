valores = []
valores.append(5)
valores.append(9)
valores.append(3)
for c in range(0,5):
	valores.append(int(input('Digite um valor')))

for c, v in enumerate(valores):
	print(f'na posiçao {c} encontrei o valor {v}!')
print('chguei ao final da lista')
