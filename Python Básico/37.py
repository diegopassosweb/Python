num = int(input('Digite um numero inteiro: '))
print('''
[ 1 ] converter para BINARIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL ''')
opt = int(input('Sua opção: '))
if opt == 1:
    print(f'Convertendo {num} para BINARIO: {bin(num) [2:]}')
elif opt == 2:
    print(f'Covertendo {num} para OCTAL {oct(num) [2:]}')
elif opt == 3:
    print(f'Covertendo {num} para HEXADECIMAL {hex(num) [2:]}')
else:
    print('Fim')