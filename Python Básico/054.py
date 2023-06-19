from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0
for pess in range(1, 8):
    nasc = int(input('Ano de nascimento: '))
    idade = atual - nasc
    if idade >= 21:
        print('Maior de idade')
        totmaior =+ 1
    else:
        print('Menor de idade')
        totmenor += 1
print(f'Ao todo tivemos {totmaior} pessoas com maior idade')
print(f'Ao todo tivemos {totmenor} pessoas com menor idade')