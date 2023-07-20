from random import randint
v = 0
while True:
    jog = int(input('Digite um valor: '))
    pc = randint(0, 11)
    tot = jog + pc
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Impar? ')).strip().upper()[0]
    print(f'Voce jogou {jog} e o computador {pc}, total de {tot}')
    if tipo == 'P':
        if tot % 2 == 0:
            print('VOCE VENCEU!')
            v += 1
        else:
            print('VOCE PERDEU!')
            break
    elif tipo == 'I':
        if tot % 2 == 1:
            print('VOCE VENCEU!')
            v += 1
        else:
            print('VOCE PERDEU!')
            break
    print('Vamos jogar novamente...')
print(f'GAME OVER! Voce venceu {v} vezes')