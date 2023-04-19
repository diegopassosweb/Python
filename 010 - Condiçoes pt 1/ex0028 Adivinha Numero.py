from random import randint
from time import sleep #faz o computador esperar
pc = randint(0,5) #sorteia um numero entre 0 - 5 
print('=='*20)
print('Vou pensar em um numero entre 0 e 5. Tente adivinhar...')
print('=='*20)
ps = int(input('Em que numero eu pensei? '))
print('Hummm....')
sleep(2)
if ps == pc:
    print('PARABENS! Voce ganhou! ')
else:
    print(f'DERROTADO! Eu pensei no numero {pc}')
