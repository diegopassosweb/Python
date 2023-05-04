jogador = dict()
time = list()
partidas = list()

while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome do jogador: '))
    tot = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    partidas.clear()
    for c in range(0, tot):
        partidas.append(int(input(f' Quantos gols na partida {c+1}? ')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())
    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper()[0]
        if resp in 'SN':
            break
        print('Erro! S ou N')
    if resp == 'N':
        break
print('-='*30)
print('cod ', end="")
for i in jogador.keys():
    print(f'{i:<15}', end="")
print()
print('-='*40)
for k, v in enumerate(time):
    print(f'{k:>3} ', end="")
    for d in v.values():
        print(f'{str(d):<15}', end="")
    print()
print('-='*40)
while True:
    busc = int(input('Mostrar dados de qual jogador? (999: stop): '))
    if busc == 999:
        break
    if busc >= len(time):
        print(f'Erro sem jogador com codigo {busc}')
    else:
        print(f' ---- LEVANTAMENTO DO JOGADOR {time[busc]["nome"]}:')
        for i, g in enumerate(time[busc]['gols']):
            print(f'    No jogo {i+1} fez {g} gols')
    print("-="*40)