# import math
# num = int(input('Digite um numero: '))
# raiz = math.sqrt(num)
# print(f'A raiz de {num} é igual a {math.ceil(raiz)}')


# from math import sqrt, floor
# num = int(input('Digite um numero: '))
# raiz = sqrt(num)
# print(f'A raiz de {num} é igual a {floor(raiz)}')

from math import floor, trunc

num = float(input('Digite um numero: '))
print(f'O valor digitado foi {num} e sua porçao inteira é {floor(num)}')
print(f'O valor digitado foi {num} e sua porçao inteira é {trunc(num)}')
print(f'O valor digitado foi {num} e sua porçao inteira é {int(num)}')