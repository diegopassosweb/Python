from random import randint
vit = 0
cont = 'N'
while True:
    jog = int(input('Digite um valor: '))
    pc = randint(0,11)
    tot = jog + pc
    tip = ' '
    while tip not in 'PI':
        tip = str(input('Par ou Impar? [P/I] ')).strip().upper()[0]
    print(f'Voce jogou {jog} e o pc {pc}, total de {tot}')
    print(f'DEU PAR' if tot % 2 == 0 else 'DEU IMPAR')
    if tip == 'P':
        if tot % 2 == 0:
            print('VOCE VENCEU!')
            vit += 1
        else:
            print('VOCE PERDEU!')
            break
    elif tip == 'I':
        if tot % 2 == 1:
            print('VOCE GANHOU!')
            vit += 1
        else:
            print('VOCE PERDEU!')  
            break
    
print(f'GAME OVER! Voce venceu {vit} vezes')


    
    