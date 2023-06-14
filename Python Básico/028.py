from random import randint
from time import sleep
pc = randint(0,5)

n = int(input("Digite um numero: "))
print('Verificando...')
sleep(2)
if pc == n:
    print('PARABENS! Voce acertou!')
else:
    print(f'GANHEI! Pensei no numero: {pc}')