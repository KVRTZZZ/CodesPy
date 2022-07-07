c = float(input('qual é o valor da casa que voce quer comprar? \nR$'))
s = float(input('qual e o valor do seu salario atual? \nR$'))
a  = int(input('em quantos você quer anos pagar?\n'))
p = c/ (a * 12)
mi = s*30/100
#print(f'para pagar uma casa de R${c:.2f} em {a} anos\n Voce tera que pagar uma prestação de {p:.2f}')
if a >10:
	print('infelizmente nao financiamos casas com mais de 10 anos de prestações ')
elif p >mi:
	print('negado')
elif p <mi:
	print('aceito')
	print(f'para pagar uma casa de R${c:.2f} em {a} anos\nVoce tera que pagar uma prestação de {p:.2f}')