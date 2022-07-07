print('parabens você foi promovido e ganhou aumento salarial!!!\n')
salario = float(input ('qual é o seu salário atual?\n'))
if (salario <= 500):
	novo = salario + (salario*15/100)
	print(f'seu novo salário é de {novo:.2f}')
if salario >500 and salario <1000:
	novo = salario +(salario*10/100)
	print(f'seu novo salário é de {novo:.2f}')
if salario >=1000:
	novo = salario + (salario*5/100)
	print(f'seu novo salário e de {novo:.2f}')
print ('\t ----PARABÉNS----')
