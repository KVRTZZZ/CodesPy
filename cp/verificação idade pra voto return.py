def voto(aniversario):
    '''
    CORRIGIR CODIGO DEPOIS, ERRO DE VERIFICAÇÃO DE IDADE, TALVEZ SEJA BUG, OU NAO
    '''
    from datetime import date 
    ano = date.today().year
    idade = ano - aniversario
    if idade < 16:
        return f'Com {idade} anos de idade: VOTO NEGADO'
    elif 16 <= idade < 18 or idade > 65:
        return f'com {idade} anos de idade seu voto: OPCIONAL'
    else:
       return f'com {idade} anos de idade, seu voto é: OBRIGATORIO)))'
       
        
        
        
print('quando você nasceu ?')
while True: 
    q = int(input())
    print(voto(q))
    help(voto)