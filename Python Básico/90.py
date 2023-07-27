aluno = dict()
aluno['nome'] = str(input('Nome: '))
aluno['media'] = float(input(f'Media do {aluno["nome"]}: '))
if aluno['media'] > 7:
    aluno['situaçao'] = 'Aprovado'
elif 5 <= aluno['media'] < 7:
    aluno['situaçao'] = 'Recuperaçao'
else:
    aluno['situaçao'] = 'Reprovado'
print()
for k, v in aluno.items():
    print(f'{k} é igual a {v}')
