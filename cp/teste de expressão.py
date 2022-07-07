lista = []
exp = str(input('digite uma expressão: '))
for c in exp:
    if c == '(':
        lista.append(c)
    elif c == ')':
        if len(lista) > 0:
            lista.pop()
        else:
            lista.append(')')
            break
print('lista',lista)
if len(lista) == 0:
    print('valido')
else:
    print('invalido')