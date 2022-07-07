def soma (* valores):
    s = 0
    for num in valores:
        s += num
    print(f'somando os valores {valores} temos {s}')
    
    
soma(1, 2, 3)
soma(4, 3)
soma(8, 2)