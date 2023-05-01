times = ("Corinthians", "Palmeiras", "Santos", "Gremio",
         "Cruzeiro", "Flamengo", "Vasco", "Chapecoense", "Atletico",
         "Botafogo", "Atletico-PR", "Bahia", "Sao Paulo", "Fluminense",
         "Sport Recife", "EC Vitoria", "Coritiba", "Avai", "Ponte Preta",
         "Atletico-GO")

print("-="*15)
print(f'Lista de times {times}')
print("-="*15)
print(f'Os 5 primeiros sao {times[0:5]}')
print("-="*15)
print(f'Os 4 ultimos sao {times[-4:]}')
print("-="*15)
print(f"Em ordem alfabetica {sorted(times)}")
print("-="*15)
print(f'Chapecoense esta na {times.index("Chapecoense") + 1} posiçao')
#for t in times:
#print(t)