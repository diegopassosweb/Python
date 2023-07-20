p = int(input('Primeiro termo: '))
r = int(input('Razao: '))
t = p
cont = 1
tot = 0
mais = 10
while mais != 0:
    tot = tot + mais
    while cont <= tot:
        print(f'{t} => ', end='')
        t += r
        cont += 1
    mais = int(input('Quantos termos a mais? '))
print(f'Finalizando com {tot} termos')