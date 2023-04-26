
print('-=' * 10)
p = int(input('Primeiro termo: '))
r = int(input('Razao da PA: '))
termo = p
cont = 1
while cont <= 10:
    print(f' {termo} => ', end="")
    termo += r
    cont += 1