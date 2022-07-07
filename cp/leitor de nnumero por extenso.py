ext = 'zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quize', 'dezeseis', 'dezesete', 'dezoito', 'dezenove', 'vinte'
while True:
	q = int(input('Digite um numero entre 0 e 20:\n'))
	if q < 0 :
		print('Digite um numero maior,  entre 0 e 20:\n')
		q = int(input(''))
	elif q > 20:
		print('Digite um numero menor, entre 0 e 20:\n')
		q = int(input(''))
	print(f'voce digitou o numero {ext[q]}')
	print('Quer continuar ?')
	sn = str(input('')).upper()
	if sn in 'NAON':
		break
	elif sn in 'SIMS':
		pass
print('fim, obrigado por usar')