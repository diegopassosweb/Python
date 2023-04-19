d = float(input('Qual a distancia da viagem? '))
print(f'Voce esta prestes a começar uma viagem de {d} km')

if d <= 200:
    p = d * 0.50
else:
    p = d * 0.45

print(f'E o preço da sua passagem sera de R${p:.2f}')