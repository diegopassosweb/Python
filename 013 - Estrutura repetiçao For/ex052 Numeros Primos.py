n = int(input('Digite um numero: '))
tot = 0
for c in range(1, n + 1):
    if n % c == 0:
        print('\033[34m', end=" ")
        tot += 1
    else:
        print('\033[31m', end=" ")    
    print(f' {c}', end=" ")
print(f'\n\033[mO numero {n} foi divisivel {tot} vezes')
if tot == 2:
    print('É PRIMO')
else:
    print('Náo é PRIMO!')