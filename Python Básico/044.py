

p = float(input("Preço das compras: R$ "))
print('''FORMAS DE PAGAMENTO
[ 1 ] á vista dinheiro/cheque
[ 2 ] á vista cartao
[ 3 ] 2x no cartao
[ 4 ] 3 ou mais no cartao''')
op = int(input("Qual opçao? "))
if op == 1:
    total = p - (p * 10 / 100)
elif op == 2:
    total = p - (p * 5 / 100)
elif op == 3:
    total = p 
    par = total / 2
    print(f'Sua compra sera parcelada em 2x de R$ {par:.2f}')
elif op == 4:
    total = p + (p * 20 / 100)
    totalpar = int(input('Quantas parcelas? '))
    par = total / totalpar
    print(f'Sua compra sera parcelada em {totalpar}x de R$ {par:.2f} COM JUROS')
else:
    total = 0
    print('Erro opçao invalida')
print(f'Sua compra de R$ {p:.2f} vai custar R$ {total:.2f} no total')