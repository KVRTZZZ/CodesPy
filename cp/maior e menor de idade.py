from datetime import date
hj = date.today().year
ma = 0
me = 0
for c in range (1,8):
	q = int(input(f'digite o ano a {c}° nasceu? '))
	idade = hj - q 
	if idade >= 21:
		ma += 1
	else:
		me +=1
print(f'temos {ma} maiores')
print(f'e tivemos {me} menores')