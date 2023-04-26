
print('-=' * 10)
p = int(input('Primeiro termo: '))
r = int(input('Razao da PA: '))
termo = p
cont = 1
tot = 0
m = 10
while m != 0:
    tot = tot + m
    while cont <= tot:
        print(f' {termo} => ', end="")
        termo += r
        cont += 1
    print('Pausa')
    m = int(input('Quantos termos quer a mais? '))
print(f'Fim, finalizamos com {tot} termos')