from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0
for pessoas in range(1, 3):
    nasc = int(input(f'Em que ano a {pessoas} pessoa nasceu: '))
    idade = atual - nasc
    if idade >= 21:
        totmaior += 1
    else:
        totmenor += 1
print(f'Ao todo tivemos {totmaior} maiores de idade')
print(f'Ao todo tivemos {totmenor} menores de idade')
