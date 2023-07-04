import moedas3

p = float(input('Digite o preço: R$ '))
print(f'A metade de {moedas3.moeda(p)} é {moedas3.metade(p, True)}')
print(f'O dobro de {moedas3.moeda(p)} é {moedas3.dobro(p, True)}')
print(f'Aumentando 10%, temos {moedas3.aumentar(p, 10, True)}')
print(f'Reduzindo em 13%, temos {moedas3.diminuir(p, 13, True)}')