
n = int(input("Digite um numero INT: "))
print('''Escolha uma das bases para conversao:
[ 1 ] converter para BINARIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL''')
op = int(input("Sua opção: "))
if op == 1:
    print(f'{n} convertido para BINARIO é igual a {bin(n)[2:]}')
elif op == 2:
    print(f'{n} convertido para OCATAL é igual a {oct(n)[2:]}')
elif op == 3:
    print(f'{n} convertido para HEXADECIMAL é igual a {hex(n)[2:]}')
else:
    print('Opção invalida!')