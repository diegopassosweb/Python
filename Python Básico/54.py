from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0
for c in range(1, 3):
    nasc = int(input(f'Ano de nascimento da {c} pessoa: '))
    idade = atual - nasc
    if idade >= 21:
        totmaior += 1
        print('Maior de idade')
    else:
        totmenor += 1
        print('Menor de idade')
print(f'Ao todo tivemos {totmaior} maiores de idade e {totmenor} menores')