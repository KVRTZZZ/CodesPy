teste = ['brasil','chile','mongolia']
acertos = []
tentativas = 0
print('Bem vindo ao jogo de adivinhação de países')
print('sua missão é acertar os paises')
print('digite o nome dos países corretamente')
while True:
    tent= str(input('digite o nome de um país\n'))
    
    if tent in acertos:
        print( 'você já digitou esse país\n')
        tentativas += 1
        
    elif tent not in teste:
       print('esta errado, verifique se digitou corretamente ou se esse país existe\n')
       tentativas +=1
      
    else:
        print('parabens, esta correto\n')
        acertos.append(tent)
        tentativas += 1
    
    
    
    if len(acertos) == 3:
        print('voce acertou tudo')
        print('parabens')
        break
print(f'foram nescessário, {tentativas} para acertar todos os 3 países:')