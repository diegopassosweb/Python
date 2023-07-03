
def leiaint(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[0:31mERRO! Digite um numero int valido \033[m')
        if ok:
            break
    return valor

n = leiaint('Digite um numero: ')
print(f'Voce digitou o numero {n}')