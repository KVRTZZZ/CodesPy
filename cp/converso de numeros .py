num = int(input('digite um numero inteiro: \n'))
print('''escolha uma das bases para conversão:
[1] converter para BINARIO
[2] converter para OCTAL
[3] converter para HEXADECIMAL''')
o = int(input('\nSua escolha \n'))
if o == 1:
	print(f'{num} em binario é {bin(num)[2:]}')
elif o == 2:
	print(f'{num} convertido para OCTAL é {oct(num)[2:]}')
elif o == 3:
	print(f'{num} convertido para hexadecimal é {hex(num)[2:]}')
else:
	print('tente novamente')