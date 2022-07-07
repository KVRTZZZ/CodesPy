import random 
n =random.randint(0,10)
certo = False
co = 0
while not certo:
	player = int(input('digite seu palpite: '))
	co += 1
	if player == n:
		certo = True
print(f'parabens, foram nescessarios {co} palpites')