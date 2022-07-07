maior = 0
menor = 0

n1= float(input('digite um numero: '))
n2 = float(input('digite outro numero: '))
print('\n')
menu  = ('''[1]  Soma
[2]  Multiplicacão
[3]  Maior ou menor
[4]  Novos numeros
[5]  Encerrar programa
''')
print(menu)
user = int(input('digite o numero da opção que você deseja\n'))
print('\n')
while user != 5: 
	if user > 5:
		print('escolha uma opção de 1 a 5 por favor')
		print('\n')
		
		print(menu)
		user = int(input(''))
	elif user <= 0:
		print('digite uma opção entre 1 a 5, por favor')
		print('\n')
		print(menu)
		user = int(input(''))
	else:
			if user == 1:
				r = n1 + n2
				print(f'\nO resultado da soma entre os dois e {r}\n')
				print(menu)
				user = int(input(''))
			elif user == 2:
				m = n1 * n2
				print(f'\nO resultado da multiplicação entre os dois numeros é {m}\n')
				print(menu)
				user = int(input(''))
			elif user ==3:
				if n1 > n2 :
					maior = n1
					menor = n2
					print(f' {n1} é maior que {n2}\n')
					
					print(menu)
					user = int(input(''))
				elif n2 > n1:
					maior = n2
					menor = n1
					print(f'{n2} é maior que {n1}\n')
					
					print(menu)
					user = int(input(''))
				elif n1 == n2 :
					print('\nOs valores sao iguais\n')
					
					print(menu)
					user = int(input(''))
			elif user == 4:
				new1 = float(input('Digite o novo numero: '))
				new2 = float(input('Digite o outro novo numero: '))
				print('\n')
				n1 = new1
				n2 = new2
				print(menu)
				user = int(input(''))
					
			elif user == 5:
					print('')
print('Obrigado por usar\nPrograma encerrado') 