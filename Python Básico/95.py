jogador = dict()
partidas = list()
time = list()

while True:
    jogador['nome'] = str(input('Nome do jogador: '))
    tot = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    partidas.clear()
    for c in range(0, tot):
        partidas.append(int(input(f' Quantos gols na partida {c+1}? ')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())
    while True:
            r = str(input('Continuar? [S/N] ')).upper()[0]
            if r in 'SN':
                break
            print('Erro digite S ou N')
    if r == 'N':
        break
print('cod ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
for k, v in enumerate(time):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print()
while True:
    busc = int(input('Mostrar dados de qual jogador? '))
    if busc == 999:
        break
    if busc >= len(time):
        print(f'ERRO Nao existe jogador com codigo {busc}')
    else:    
        print(f'levantamento do jogador {time[busc]["nome"]}: ')
        for i, g in enumerate(time[busc]["gols"]):
            print(f'         No jogo {i} fez {g} gols')
    print()
    