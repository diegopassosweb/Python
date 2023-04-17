#Faca um programa que leia um angelo qualquer e mostre na tela o valor do
# seno, coseno e tangente desse angulo.
import math
from math import radians, sin, cos, tan
angulo = float(input('Digite um angulo que voce desejar: '))
seno = math.sin(math.radians(angulo))
print(f'O angulo de {angulo} tem o seno de {seno:.2f}')
cosseno = math.cos(math.radians(angulo))
print(f'O angulo de {angulo} tem o cosseno de {cosseno:.2f}')
tangente = math.tan(math.radians(angulo))
print(f'O angulo de {angulo} tem o tangente de {tangente:.2f}')

