while True:
    print('digite um valor para saber sua potência de "i"\n[999 para parar]')
    q = int(input(''))
    if q % 4 == 0:
        print()
        print('1')
        print()
    if q % 4 == 1:
        print()
        print('i')
        print()
    if q % 4 == 2:
        print()
        print('-1')
        print()
    if q % 4 == 3:
        print()
        print('-i')
        print()
    if q == 999:
        break
print('cabou')