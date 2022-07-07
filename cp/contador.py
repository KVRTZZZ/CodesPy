bfrom time import sleep


def contador(ini, fim, passo):
    print(f'contagem de {ini}, até {fim}, de {passo}, {passo}'
    cont = ini
    while cont <= fim:
        print(f'{cont}', end = ',' )
        cont += passo
    print('fim')
    
    
contador(1, 10, 1)