from datetime import datetime
dados = dict()
dados['nome'] = str(input('Nome: '))
nasc = int(input('Ano de Nascimento: '))
dados['idade'] = datetime.now().year - nasc
dados['ctps'] = int(input('Carteira de Trabalho (0: nao tem): '))
if dados['ctps'] != 0:
    dados['contrat'] = int(input('Ano de Contrataçao: '))
    dados['salario'] = float(input('Salario: R$'))
    dados['aposent'] = dados['idade'] + ((dados['contrat'] + 35) - datetime.now().year)
print('-='*30)
for k, v in dados.items():
    print(f'  - {k} tem o valor {v}')