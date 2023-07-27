from random import randint
from time import sleep
from operator import itemgetter
jogo = {'jogador1': randint(1,6), 
        'jogador2': randint(1,6), 
        'jogador3': randint(1,6),
        'jogador4': randint(1,6), 
        'jogador5': randint(1,6), 
        'jogador6': randint(1,6)}
ranking = list()
print('Valores sorteados: ')
for k, i in jogo.items():
    print(f'{k} tirou {i}')
    sleep(1)
print()
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
for i, v in enumerate(ranking):
    print(f'{i+1}lugar: {v[0]} com {v[1]} ')
    sleep(1)