def leiaint(a):
    a = input(a)
    while True:
        if a.isdigit():
            n = int(a)
            return n
        else:
            a = input    ('\033[0;31mdigite um número válido\033[m\n')
                
print('\tteste de raiz')
print('Levando a seguinte equação a seguir F(x) = x² -5x +6\n')
while True:
    num = leiaint('')
    teste = (num**2 )-5*num + 6
    if teste == 0:
        print(f'é uma função, pois o resultado é {teste}\n')
    else:
        print(f'nao é uma função, pois o resultado é {teste}\n')