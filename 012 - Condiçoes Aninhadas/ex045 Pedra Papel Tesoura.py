from random import randint
itens = ('Pedra', 'Papel', 'Tesoura')
pc = randint(0, 2)
print('''Suas opçoes:
      [ 0 ] PEDRA
      [ 1 ] PAPEL
      [ 2 ] TESOURA''')
player = int(input('Qual é sua jogada? '))

print(f'O computador escolheu {itens[pc]}')
print(f'O jogador jogou {itens[player]}')
if pc == 0:
    if player == 0:
        print('EMPATE')
    elif player == 1:
        print('JOGADOR VENCE')
    elif player == 2:
        print('PC VENCE')
    else:
        print('JOGADA INVALIDA!')
elif pc == 1:
    if player == 0:
        print('PC VENCE')
    elif player == 1:
        print('EMPATE')
    elif player == 2:
        print('JOGADOR VENCE')
    else:
        print('JOGADA INVALIDA!')
elif pc == 2:
    if player == 0:
        print('JOGADOR VENCE')
    elif player == 1:
        print('PC VENCE')
    elif player == 2:
        print('EMPATE')
    else:
        print('JOGADA INVALIDA!')