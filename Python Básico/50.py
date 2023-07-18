s = 0
cont = 0
for c in range(1, 7):
    n = int(input('Digite um numero: '))
    if n % 2 == 0:
        s += n
        cont += 1
print(f'Voce informou {cont} numeros pares, e a soma foi {s}')