print('parabens voce foi escolhido para um aumento salarial!!!\n')
s=float(input('digite qual é o seu salario atual:\n'))
if s <= 1250:
	c = s + (s * 15/100)
	print (f'o seu novo salario e de {c}')
else:
	r = s+ (s * 10/100)
	print(f'o seu novo salario e de {r}')
print('\t parabens')