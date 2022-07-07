q = str(input('digite seu palindromo\n')).upper()
q  = ''.join(q.split(' '))
if q == q[::-1]:
	print(f'é palindromo pois {q} é a mesma coisa ao contrario')
else:
	print(f'nao e palindromo pois e {q}')