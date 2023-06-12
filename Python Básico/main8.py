
from math import sqrt, floor

num = int(input("Digite um numero: "))
# raiz = math.sqrt(num)
raiz = sqrt(num)
# print(f'A raiz de {num} é {math.ceil(raiz)}')
print(f'A raiz de {num} é {floor(raiz)}')
print(f'A raiz de {num} é {raiz:.2f}')
print(f'A raiz de {num} é {raiz}')