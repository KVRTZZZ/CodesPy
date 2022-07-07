print('digite quantos KMs é a sua viagem! ')
v = float(input('Digite: '))
if v <=200:
	preco = (v*0.50)
else:
	preco = (v*0.45)
print(f'o preco da sua passagem vai custar R${preco}')