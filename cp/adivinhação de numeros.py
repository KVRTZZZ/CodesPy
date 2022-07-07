import  random 
c = random.randint(0, 5)
print('-º '* 20)
print('eu estou pensando em um numero de 0 a 5, tente advinhar qual é')
print('-º '* 20)

n = int(input('\nem qual numero eu estou pensando?\n'))
if c == n:
	print('Parabens voce acertou!')
else:
	print(f'voce errou, o numero que eu estou pensando é {c}, tente novamente!')