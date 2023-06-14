
d = float(input("Qual é a distancia de sua viagem? "))
print(f'Voce esta prestes a começar uma viagem de {d} Km')
if d <= 200:
    p = d * 0.50
else:
    p = d * 0.45
print(f'O preço sera de R${p:.2f}')