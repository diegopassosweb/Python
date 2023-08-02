import moed

p = float(input('Digite o preço: R$ '))
print(f'A metade de {p} é R${moed.metade(p)}')
print(f'O dobro de {p} é R${moed.dobro(p)}')
print(f'Aumentando 10%, temos R${moed.aumentar(p, 10)}')