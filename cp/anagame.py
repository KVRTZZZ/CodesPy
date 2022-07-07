from time import sleep
print('Voce esta em um pequeno RPG criado por alguem cujo nao tem nada para fazezr')
sleep(3)
print('criado"Kurtzzz"\n')
print('Qual é o seu nome?')


nome = str(input())
print('Belo nome')
sleep(1)
print('vamos começar')
print('\n')



sleep(2)
print('você acorda com batidas na porta do seu quarto, e escuta uma voz fina chamando seu nome ')
sleep(1)
print(nome.upper())
sleep(2)
print(nome.upper())
print('\n')
print('voce logo percebe que é a ana, sua irma')
print('\n')
print('ela esta tentando te avisar algo, mas voce nao entende')
sleep(2)




def menu1():
    return  '''[1] abrir a porta do seu quarto
[2] ir ao banheiro
[3] ir dar bom dia para sua mãe, ignorando sua irmã'''

def menu2():
       return  '''[2] ir ao banheiro
[3] ir ver sua mãe, ignorando sua irmã'''

def menu3():
    return   '''[3] ir ver sua mãe, ignorando sua irmã'''

print('o que você faz ?\n')
print(menu1())
print('\n')
user = int(input(''))


while user > 3 or user < 0:
    print('opção invalida, tente de novo')
    user = int(input('')) 
    
    
if user == 1:
	print('\nana vem em sua direção e te da um chute em sua perna por ter feito ela esperar, mas depois te da um abraço e um bom dia.\nEm seguida ela corre para a cozinha ir ver sua mae\n')
	
	
	print('''[2] ir ao banheiro
[3] ir ver sua mãe''')

	user = int(input('o que voce faz?: '))
	
	while user < 2 or user > 3:
		print('opçao invalida bobãoo,')
		user = int(input('tenta de novo: '))
		
		if user == 2:
			print('você vai ao banheiro, escova seus dentes e volta para o quarto\n')
			sleep(1)
			print('''[3] ir ver sua mãe''')
			user = int(input(' oque voce deseja fazer agora? '))
			
			while user != 3:
				print('tenta de novo')
				user = int(input(''))
				
				
			if user == 3:
				print('\nV)oce esta indo em direção a cozinha, mas aparece voce sabe quem do alem com uma espcie de peixe na mão, ele te encara por alguns segundos e em seguidae conjura um Avada Kedavra em você\nEle começa a murmura algo como "na.... se.. faz... mais ch..ves de port... como antigam... e depois desaparece')
				print('''[3] ir ver sua mãe''')
				user == int(input('oque voce deseja fazer ?: '))
				
				
		if user == 3:
			print('voce ja fez isso, nao se lembra ?')
			print('''[3] ir ver sua mãe''')
			user == int(input('oque voce deseja fazer ?: '))
			
			
	if user == 3:
				print('voce ja fez isso, nao se lembra ?')
				print('''[3] ir ver sua mãe''')
				user == int(input('oque voce deseja fazer ?: '))	
				
					
elif user == 2:
	print('você vai ao banheiro, escova seus dentes e volta para o quarto')
	sleep(1)
	print('Ana percebe que voce ta ignorando ela e fica triste, voce escuta ela sair choramingando\n')
	print('Voce abre a porta depois de muito tempo, mas não ve ninguem\n')
	print('voce decide voltar para o seu quarto')
	print('''[3] ir ver sua mae''')
	print('\t')
	user = int(input('o que voce deseja fazer agora? '))
	while user != 3:
		print('nao tem essa opção burro')
		user = int(input('tenta de novo: '))
		if user == 3:
			print('\nV)oce esta indo em direção a cozinha, mas aparece voce sabe quem do alem com uma espcie de peixe na mão, ele te encara por alguns segundos e em seguidae conjura um Avada Kedavra em você\nEle começa a murmura algo como "na.... se.. faz... mais ch..ves de port... como antigam... e depois desaparece')
		
elif user == 3 :
	print('voce olha sua irmã de braços abertos esperando um abraço seu, mas vc passa reto')
	print('ela pega o vaso de planta atras de ti, taca na sua cabeça e voce morre')
print('fim')