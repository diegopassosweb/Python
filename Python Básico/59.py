from time import sleep
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
opt = 0
while opt != 5:
    print('''
    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novo numeros
    [ 5 ] sair do programa''')
    opt = int(input('Qual é a sua opção? '))
    if opt == 1:
        soma = n1 + n2
        print(f'A soma entre {n1} e {n2} é {soma}')
    elif opt == 2:
        produto = n1 * n2
        print(f'O resultado de {n1} x {n2} é {produto}')
    elif opt == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print(f'Entre {n1} e {n2} o maior é {maior}')
    elif opt == 4:
        print(f'Informe os numeros novamente! ')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif opt == 5:
        print('Finalizando...')
    else:
        print('Opção invalida!')
    sleep(1)
print('Fim do programa')

