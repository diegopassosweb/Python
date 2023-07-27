
filme = {'titulo': 'Star Wars', 'ano': 1977, 'diretor': 'Geoge Lucas'}
print(filme.values()) #pega valores
print(filme.keys()) # pega as chaves
print(filme.items()) # pega ambos
for k, v, in filme.items():
    print(f'O {k} é {v}')

