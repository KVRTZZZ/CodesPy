lista = []
for n in range (0,5):
	lista.append(int(input(f'digite uma valor para a posição {n}: ')))
	
for n , v in enumerate(lista):
	print(f'\nNa posiçao {n} encontreei o numero {v}\n')
print(f'O maior valor digitado foi {max(lista)}')
print(f'O menor valor digitado foi {min(lista)}')