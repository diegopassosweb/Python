n = 1
impar = 0
par = 0
while n != 0:
    n = int(input('Digite um valor: '))
    if n != 0:
        if n % 2 == 0:
            par += 1
            print(f' {n} é Par')
        else:
            impar += 1
            print(f'{n} é Impar')
print(f'Voce digitou {par} numeroes pares e {impar} impares')