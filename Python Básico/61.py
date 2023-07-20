p1 = int(input('Primeiro termo: '))
r = int(input('Razao: '))
t = p1
cont = 1
while cont <= 10:
    print(f'{t} => ', end='')
    t += r
    cont += 1
    