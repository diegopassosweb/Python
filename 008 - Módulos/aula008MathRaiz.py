import math #IMPORTANDO TODAS AS FUNCIONALIDADES
from math import sqrt, floor ## IMPORTANDO O METODO SQRT FLOOR
num = int(input('Digite um numero: '))
raiz = math.sqrt(num)
raiz = sqrt(num) #somente sqrt
print(f'A raiz de {num} é igual a (para cima) {math.ceil(raiz)} ')
print(f'A raiz de {num} é igual a (para baixo) {math.floor(raiz)} ')
print(f'A raiz de {num} é igual a (2 casas) {raiz:.2f} ')
print(f'A raiz de {num} é igual a (somente floor) {floor(raiz)} ')
