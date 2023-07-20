from random import randint
pc = randint(0, 10)
print('Sou o computador. Acabei de pensar em um numero entre 0 e 10')
print('Sera que consegue adivinhar qual foi? ')
acertou = False
palpites = 0
while not acertou:
    jog = int(input('Qual o seu palpite? '))
    palpites += 1
    if jog == pc:
        acertou = True
    else:
        if jog < pc:
            print('Mais...')
        elif jog > pc:
            print('Menos...')
print(f'Acertou com {palpites} tentivas')