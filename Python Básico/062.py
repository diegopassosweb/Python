
p = int(input('Primeiro termo: '))
r = int(input('Razao: '))
t = p
mais = 10
tot = 0
cont = 1
while mais != 0:
    tot = tot + mais
    while cont <= tot:
        print(f'{t} => ', end='')
        t += r
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos voce quer a mais? '))
print(f'Finalizado com {tot} termos ')
print('fim')