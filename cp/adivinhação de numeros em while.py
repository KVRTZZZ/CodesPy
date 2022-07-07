import random
import time 

ce = 0
er = 1

num = int(input('em qual numero eu pensei?\n'))

n = random.randint(0,10)

while num != n:
	if num < 0 or num > 10:
		if num < 0: 
			print('o numero nao pode ser negativo!')
			num = int(input('digite \n'))
			er += 1
		elif num > 10:
			print('nao pode ser um numero maior que 10')
			num = int(input('digite\n')) 
			er += 1
	else:
		if num > n:
			print('tenta um numero menor')
			num = int(input('tente novamente: '))
			er += 1
		elif num < n:
			print('tente um numero maior')
			num = int(input('tente novamente: '))
			er +=1
		elif num == n:
			print('voce acertou o numero')
			break 
print(f'foram nescessario {er} palpites para acertar o numero')