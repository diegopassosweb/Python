maior = 0
menor = 0
for p in range(1, 3):
    peso = float(input(f'Peso da {p} pessoa: '))
    if p == 1:
        maior += peso
        menor = peso
else:
    if peso > maior:
        maior = peso
    if peso < menor:
        menor = peso
print(f'O maior peso foi de {maior} KG')
print(f'O menor peso foi de {menor} KG')