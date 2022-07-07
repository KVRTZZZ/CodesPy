def leiaint(a):
    a = input(a)
    while True:
        if a.isdigit():
            return a
        else:
            a = input('erro, tente novamente')
           
           
a = leiaint('Digite um numero: ')
print(f'voce digitou o numero {a+1}')