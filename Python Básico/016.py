
# import math
from math import trunc
ask = str(input("Com metodo math ou padrão?: [M/P]"))
num = float(input("Digite um numero: "))
if ask == "M" or "m":
# print(f'O valor digitado foi {num} e sua porção inteira é {math.trunc(num)}')
    print(f'O valor digitado foi {num} e sua porção inteira é {trunc(num)}')
elif ask == "P" or "p":
    print(f'O valor digitado foi {num} e sua porção inteira é {int.num}')


