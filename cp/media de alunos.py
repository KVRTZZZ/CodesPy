aluno = dict()
aluno ['nome'] = str(input('Nome: '))
aluno['média'] = float(input('media '))
if aluno['média'] >= 7:
    aluno['situação'] = 'provado'
elif 5 <= aluno['media'] < 7:
    aluno['situação'] = 'recuperação'
else:
    aluno['situacao'] = 'reprovado'
for k, v in aluno.items():
    print(f'o aluno {k} é igual a {v}')
    