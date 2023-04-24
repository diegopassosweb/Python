first = int(input('Digite um numero: '))
second = int(input('Digite outro numero: '))
if first > second:
    print(f'O primeiro valor é maior')
elif second > first:
    print(f'O segundo valor é maior')
else:
    print('Não existe valor maior, os dos sao iguais')