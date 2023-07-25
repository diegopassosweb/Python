num = list()
par = list()
impar = list()
while True:
    num.append(int(input('Digite um numero: ')))
    r = str(input('Quer continuar? [S/N] '))
    if r in 'Nn':
        break
for i, v in enumerate(num):
    if v % 2 == 0:
        par.append(v)
    elif v % 2 == 1:
        impar.append(v)

print(f'Os valores digitados foram {num}')
print(f'A lista de pares é {par}')
print(f'A lista de impares é {impar}')