
p = int(input('Primeiro termo: '))
r = int(input('Razao: '))
t = p
cont = 1
while cont <= 10:
    print(f'{t} => ', end='')
    t += r
    cont += 1
print('fim')