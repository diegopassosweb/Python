#Sorteando um item na lista
#Um professor quer sortear um do seus quatro alunos para apagar o quadro.
#faca um programa que ajude ele,lendo o nome deles e escrevendo o nome do escolhido

import random
n1 = str(input('Primeiro Aluno: '))
n2 = str(input('Primeiro Segundo: '))
n3 = str(input('Primeiro Terceiro: '))
n4 = str(input('Primeiro Quarto: '))
lista = [n1,n2,n3,n4]
escolhido = random.choice(lista)
print(f'O aluno escolhido foi {escolhido}')
