while True:i
	num = int(input('voce quer ver a tabuada de qual numero? '))
	print('-'*30)
	if num < 0 :
		break
	for c in range (1,11):
		print(f'{num} X {c}', '=', f'{c*num}')
	print('-'*30)
print('fim')