times = ('Corinthians', 'Palmeiras', 'Sao Paulo', 'BotaFogo', 'Fluminense', 'Vasco', 'Bahia', 'Flamengo', 'Cruzeiro', 'Chapecoense', 'Gremio', 'Santos', 'Atletico', 'Scort', 'Vitoria', 'Curitiba', 'Avai', 'Ponte Preta', 'Atletico-MG', 'Atletico-GO')

print(f'Os 5 primeros times são {times[:5]}')
print(f'Os 4 ultimos colocados são {times[-4:]}')
print(f'Os times em ordem alfabetica {sorted(times)}')
print(f'Chapecoense esta na posiçao {times.index("Chapecoense")+1}')

