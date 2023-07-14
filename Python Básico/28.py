from random import randint
pc = randint(0, 5)
print('Vou pensar em um numero entre 0 e 5, tente adivinhar...')
jog = int(input('Em que numero eu pensei? '))
if jog == pc:
    print('Parabens! Voce venceu!')
else:
    print(f'Ganhei! Pensei no numero {pc}')