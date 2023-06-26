num = list()
while True:
    n = int(input('Digite um valor: '))
    if n not in num:
        num.append(n)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado!')
    r = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if r in 'Nn':
        break
num.sort()
print(f'Voce digitou os valores {num}')