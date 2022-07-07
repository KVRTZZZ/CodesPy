 c= float(input('qual e a sua velocidade atual ?\n'))
if c <=80:
	print('parabens, continue dirigindo com segurança')
else:
	c= (c-80)*7.00
	print(f'vc passou do limite de velocidade!!! \nvc recebeu uma multa de R${c:.2f} dirija com cuidado')