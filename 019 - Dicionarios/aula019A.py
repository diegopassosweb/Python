pessoas = {"nome": "Gustavo", "sexo": "M", "idade": 22}
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos.')
del pessoas["sexo"]
pessoas['nome'] = 'Leandro'
pessoas['peso'] = 95.5
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())
for k in pessoas.keys():
    print(k)
for k in pessoas.values():
    print(k)
for k, v in pessoas.items():
    print(f'{k} = {v}')