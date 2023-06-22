
num = (int(input('Digite um numero: ')),
     int(input('Digite outro numero: ')),
     int(input('Digite mais um numero: ')),
     int(input('Digite o ultimo numero: ')))
print(F'Voce digitou os valores {num}')
print(f'O valor 9 apareceu {num.count(9)} vezes')
if 3 in num:
    print(f'O valor 3 apareceu na {num.index(3)+1} posiçao')
else:
    print('Não temos esse valor')
print('Os valores pares foram ', end='')
for n in num:
    if n % 2 == 0:
        print(n, end=' ')
