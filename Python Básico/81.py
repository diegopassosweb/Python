num = []
while True:
    num.append(int(input('Digite um valor: ')))
    r = str(input('Quer continuar? [S/N] '))
    if r in 'Nn':
        break
print(f'Voce digitou {len(num)} valores')
num.sort(reverse=True)
print(f'Os valores em ordem descrescente sao {num} ')
if 5 in num:
    print(f'O valor 5 faz parte da lista')
else:
    print('O 5 não faz parte da lista')