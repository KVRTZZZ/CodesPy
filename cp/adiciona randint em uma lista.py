from random import randint
lista = []
while len(lista) < 91:
    r = randint(10,100)
    if r not in lista:
        lista.append(r)
    else:
        continue
        
print((lista))