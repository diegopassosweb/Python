
num = (int(input('Digite um numero: ')), 
       int(input('Digite outro numero: ')), 
       int(input('Digite mais um numero: ')),
       int(input('Digite o ultimo numero: ')))
print(f'Voce digitou os valores {num}')
if 3 in num:
    print(f'O valor 9 apareceu {num.count(9)} vezes')
else:
    print('Valor não digitado')
print(f'O valor 3 apareceu na {num.index(3)+1}')
for n in num:
    if n % 2 == 0:
        print(n, end='')