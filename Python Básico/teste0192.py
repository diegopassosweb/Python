pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': 22}
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos')
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())
pessoas['nome'] = 'Leandro'
pessoas['peso'] = 90.5
for k, v in pessoas.items():
    print(f' {k} = {v}')
del pessoas['sexo']
