from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
pc = randint(0, 2)
print('''Suas opçoes:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jog = int(input('Qual é a sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO')
print('-=' * 11)
print(f'O computador jogou {itens[pc]}')
print(f'O jogador jogou {itens[jog]}')
print('-=' * 11)
if pc == 0:
    if jog == 0:
        print('EMPATE!')
    elif jog == 1:
        print('JOGADOR VENCE!')
    elif jog == 2:
        print('COMPUTADOR VENCE!')
    else:
        print('JOGADA INVALIDA!')
elif pc == 1:
    if jog == 0:
        print('COMPUTADOR VENCE')
    elif jog == 1:
        print('EMPATE')
    elif jog == 2:
        print('JOGADOR VENCE')
    else:
        print('JOGADA INVALIDA!')
elif pc == 2:
    if jog == 0:
        print('JOGADOR VENCE')
    elif jog == 1:
        print('COMPUTADOR VENCE')
    elif jog == 2:
        print('EMPATE')
    else:
        print('JOGADA INVALIDA!')
    