from datetime import date
dhj = date.today().year
nasc = int(input('digite seu ano de nascimento: '))
a = dhj - nasc
print(f'quem nasceu em {nasc} hoje tem {a} anos')
if a > 18:
	saldo = a - 18
	ano = dhj - saldo
	print(f'voce ja deveria ter se alistado a {a-18} anos, pois tem {a} anos')
	print(f'seu alistamento foi em {ano}')
elif a ==18:
	print('estar na hora de se alistar')
elif a < 18:
	saldo = 18 - a
	ano = dhj + saldo
	print(f'voce ainda nao precisa ser alistar\no alistamento é somente com 18 anos, ou seja daqui {18 - a}, em {ano}')