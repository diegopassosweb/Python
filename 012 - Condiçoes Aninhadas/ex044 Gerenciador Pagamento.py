print(f'{"Lojas Python":=^40}')
preco = float(input('Preco das compras: R$'))
print('''
[ 1 ] a vita no dinheiro/cheque
[ 2 ] a vista no cartao
[ 3 ] 2x no cartao
[ 4 ] 3x ou mais no cartao''')
opçao = int(input('Qual é a opçao? '))
if opçao == 1:
    total = preco - (preco * 10 / 100)
elif opçao == 2:
    total = preco - (preco * 5 / 100)
elif opçao == 3:
    total = preco
    parcela = total / 2
    print(f'Sua compra sera parcelada em 2x de R$ {parcela:.2f}')
elif opçao == 4:
    total = preco + (preco * 20 / 100)
    totparc = int(input('Quantas parcelas? '))
    parcela = total / totparc
    print(f'Sua compra sera parcelada em {totparc}x de R${parcela:.2f}')
    
print(f'Sua compra de R$ {preco:.2f} vai custar R${total:.2f} ')