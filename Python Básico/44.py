preco = float(input('Preço das compras: R$ '))
print('''FORMAS DE PAGAMENTO
[ 1 ] á vista dinheiro/cheque
[ 2 ] á vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
opt = int(input('Qual é a opção? '))
if opt == 1:
    tot = preco - ( preco * 10 / 100)
elif opt == 2:
    tot = preco - (preco * 5 / 100)
elif opt == 3:
    tot = preco
    par = tot / 2
    print(f'Sua compra sera parcelada em 2x de R${par}')
elif opt == 4:
    tot = preco + (preco * 20 / 100)
    totpar = int(input('Quantas parcelas? '))
    par = tot / totpar
    print(f'Sua compra sera parcelada em {totpar}x de R${par:.2f} com JUROS')
else:
    tot = preco
    print('Opção invalida!')
print(f'Sua compra de R${preco:.2f} vai custar R${tot:.2f} no final')