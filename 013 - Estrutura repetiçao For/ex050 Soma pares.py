soma = 0
cont = 0
for c in range(1, 4):
    n = int(input(f'Digite {c} valor: '))
    if n % 2 == 0:
        soma += n
        cont += 1
print(f'Voce informou {cont} numeros PARES e a soma é {soma}')