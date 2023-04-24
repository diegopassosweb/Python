num = int(input('Digite um numero inteiro: '))
print('''Escolha uma das bases para conversão: 
[ 1 ] converter para BINARIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL ''')
op = int(input('Sua opção: '))
if op == 1:
    print(f'{num} convertido para BINARIO é igual a {bin(num) [2:]}')
elif op == 2:
    print(f'{num} convertido para OCATAL é igual a {oct(num) [2:]}')
elif op == 3:
    print(f'{num} convertido para HEXADECIMAL é igual a {hex(num) [2:]}')
else:
    print('Opção invalida. Tente novamente!')