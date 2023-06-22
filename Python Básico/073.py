from time import sleep
times = ("Flamengo","Santos","Palmeiras","Gremio",
             "Atletico Paranaense", "São Paulo","Internacional",
             "Conrithians","Fortaleza","Goias","Bahia","Vasco",
             "Atletico Mineiro","Fluminense","Botafogo","Ceará",
             "Cruzeiro","CSA","Chapecoense","Avaí")
print('='* 15)
print(f'Lista de times {times}')
print('='* 15)
print(f'Os 5 primeiros sao {times[0:5]}')
print('='* 15)
print(f'Os 4 ultimos sao {times[-4:]}')
print('='* 15)
print(f'Times em ordem alfabetica {sorted(times)}')
print('='* 15)
print(f'O Chapecoense esta em {times.index("Chapecoense")+1} lugar')
