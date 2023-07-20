soma = 0
mil = 0
menor = cont = 0
barato = ''
while True:
    produto = str(input('Nome do Produto: '))
    preco = float(input('Preço: R$ '))
    cont += 1
    if preco > 1000:
        mil += 1
    soma += preco
    if cont == 1 or preco < menor:
        menor = preco
        barato = produto 
    resp = ' '
    resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print(f'Total da compra foi R$ {soma}')
print(f'Temos {mil} produtos custando mais de R$ 1000,00')
print(f'O produto mais barato foi {barato} e custa {menor}')