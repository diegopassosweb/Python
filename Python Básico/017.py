# import math
from math import hypot
co = float(input("Digite o comprimento oposto: "))
ca = float(input("Digite o comprimento adjacente: "))
# hi = (co ** 2 + ca ** 2) ** (1/2)
# print(f'A hipotenusa vai medir {hi:.2f}')
# hi = math.hypot(co, ca)
hi = hypot(co,ca)
print(f'A hipotenusa vai medir {hi:.2f}')
