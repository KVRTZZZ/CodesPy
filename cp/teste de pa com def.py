from time import sleep


def contador(início, fim, passo):
    
    for c in range(início, fim, passo):
        sleep(0.5)
        print(c, end = ', ', flush = True)
    print('fim')
        
    
    
print('_' * 30)
contador(1, 10, 1)
print('_' * 30)
contador (10, 0, -1)
print('_' * 30)
print('agora é sua vez')
i = int(input('inicio da sua contagem'))
f = int(input('digite o fim da sua contagem'))
p = int(input('digite um padrão pra sua sequência'))
contador(i,f,p)