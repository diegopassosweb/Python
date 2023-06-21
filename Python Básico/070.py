tot= totmil = menor = cont = 0
barato = ' '
while True:
    produto = str(input('Nome do produto: '))
    preço = float(input('Preço: R$'))
    cont += 1
    tot += preço
    if preço > 1000:
        totmil += 1
    if cont == 1 or preço < menor:
        menor = preço
        barato = produto
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print(f'Total da compra foi {tot:.2f}')
print(f'Temos R${totmil} produtos acima de mil reais')
print(f'O produto mais barato custa R${menor}')
print(f'O produto mais barato foi {barato}')
print(f'fim do programa')