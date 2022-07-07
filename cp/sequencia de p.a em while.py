prim = int(input("Primeiro termo: \n"))
raz = int(input("Razão da PA: \n"))
termo = prim
counter = 1
total = 0
mais = 10
while mais != 0:
	total += mais
	while counter <= total :
	    print(termo, end = ' ')
	    termo += raz
	    counter += 1
	print('Pausa')
	mais = int(input('quer continuar ? se sim, digite quanto a mais, se nao digite "0"\n'))
print(counter, 'termos foram apresentados')