'''def ficha(nome = '<desconhecido>', gol = 0):
    print(f'O jogador {nome} fez {gol} gols no campeonato')
    
    
n = str(input('digite seu nome\n'))
g = str(input('digite o número de gols\n'))

if g.isnumeric():
    g = int(g)
else:
    g = 0
    
if n.strip() == '':
    ficha(gol = g)
else:
    ficha(n,g)
    
'''    
def ficha(nome='', gol=''):
    if nome == '':
        nome = '<desconhecido>'
    if not gol.isdigit():
        gol = 0
    print(f'O jogador {nome} fez {gol} gols no campeonato')

nome = input('Nome do Jogador: ').strip().title()
gol = input('N° de gols: ').strip() 

ficha(nome, gol) 
    