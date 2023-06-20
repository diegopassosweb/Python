# from math import factorial
# n = int(input('Digite um numero: '))
# f = factorial(n)
# print(f'O fatorial de {n} é {f}')

n = int(input('Digite um numero: '))
c = n
f = 1
print(f'Calculando {n}! = ', end='')
while c > 0:
    print(f'{c}', end='')
    print(f' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print(f'{f}')