num = cont = soma = 0
num = int(input('digite um numero [0 para parar] '))
while num != 0:
	soma += num
	cont += 1
	num = int(input('digite um numero [0] para parar] ')) 
print('voce digitou', cont,'numeros, e a soma entre eles é,', soma) 