r1 = float(input('Digite o primeiro tamanho: '))
r2 = float(input('Digite o segundo tamanho: '))
r3 = float(input('Digite o terceiro tamanho: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print(f'Podem formar um triangulo')
else:
    print('Nao podem formar um triangulo')