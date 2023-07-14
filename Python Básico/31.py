dist = float(input('Qual a distancia da viagem? '))
if dist <= 200:
    preco = dist * 0.50
else:
    preco = dist * 0.45
print(f'O preço da sua passagem sera de R${preco:.2f}')
    
    