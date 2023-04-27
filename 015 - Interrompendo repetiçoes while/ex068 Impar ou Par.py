from random import randint
v = 0
while True:
    jogador = int(input('Digite um valor: '))
    pc = randint(0, 10)
    tot = jogador + pc
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Impar? [P/I] ')).strip().upper()[0]
    print(f'Voce jogou {jogador} e o computador {pc}, total de {tot}', end=" ")
    print('DEU PAR ' if tot & 2 == 0 else 'DEU IMPAR')
    if tipo == "P":
        if tot % 2 == 0:
            print('Voce VENCEU!')
            v += 1
        else:
            print('Voce PERDEU!')
            break
    elif tipo == '1':
        if tot % 2 == 1:
            print('Voce VENCEU!')
            v += 1
        else:
            print('Voce PERDEU!')
            break
        print('Fim')
print(f'GAME OVER!, Voce venceu {v} vezes')