def maior(* num):
    cont = maior = 0
    for valor in num:
        print(f'{valor}', end = ' ')
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior  = valor
        cont += 1
    print(f'o maior valor informado foi {maior}')


maior(2,5,7,9,0,6,5)
maior(2,7,9,6)
maior(272,0)
maior(0)
maior()