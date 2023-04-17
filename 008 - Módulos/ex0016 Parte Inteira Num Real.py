#Crie um programa que leia um numero Real qualquer pelo teclado e 
# mostre na tela sua porção inteira

from math import trunc
import math
num = float(input('Digite um numero: '))
print(f'A parte inteira do numero {num} é (para cima) {num:.0f}')
print(f'A parte inteira do numero {num} é {int(num)}')
print(f'A parte inteira do numero {num} é {math.trunc(num)}')
print(f'A parte inteira do numero {num} é {trunc(num)}')
