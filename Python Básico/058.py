from random import randint
pc = randint(0, 10)
print('PC... pensei em um numero entre 0 e 10, adivinha qual? ')
acertou = False
palpites = 0
while not acertou:
    player = int(input('Qual é o seu palpite? '))
    palpites += 1
    if player == pc:
        acertou = True
    else:
        if player < pc:
            print('Mais... tente novamente!')
        elif player > pc:
            print('Menos...tente novamente!')
print(f'Acertou! com {palpites} tentativas')