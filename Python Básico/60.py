# from math import factorial
# n = int(input('Digite um numero para seu Fatorial: '))
# f = factorial(n)
# print(f'O fatorial de {n} é {f}')
n = int(input('Digite um numero para seu Fatorial: '))
c = n
f = 1
while c > 0:
    print(f'{c}', end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print(f'{f}')
