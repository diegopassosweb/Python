#Sorteie uma ordem de trabalho para alunos, faca um programa que leia o nome dos quatro alunos
#e mostre a ordem dos sorteados

import random
from random import shuffle
n1 = str(input('Primeiro Aluno: '))
n2 = str(input('Primeiro Segundo: '))
n3 = str(input('Primeiro Terceiro: '))
n4 = str(input('Primeiro Quarto: '))
lista = [n1,n2,n3,n4]
random.shuffle(lista)
print(f'A ordem de apresentação sera ')
print(lista)