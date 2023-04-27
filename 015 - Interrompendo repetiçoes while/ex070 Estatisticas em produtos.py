tot = totmil = menorp = cont = 0
barato = ''
while True:
    produto = str(input('Nome do Prodto: '))
    preço = float(input('Preco: R$'))
    cont += 1
    tot += preço
    if preço > 1000:
        totmil += 1
    if cont == 1 or preço < menor:
        menor = preço
        barat0 = produto
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if resp == 'N':
        break
print('{:-^40}'.format('Fim do Programa'))
print(f'O total da compra foi R${tot:.2f}')
print(f'Temos {totmil} custando mais de mil reais')
print(f'O produto mais barato custa {menor:.2f}')
print(f'O produto mais barato foi {barato}')