
def ler(msg):
    ok = False
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[0;31mERRO, digite um numero validop\033[m')
        if ok:
            break
    return valor

n = ler('Digite um numero: ')
print(f'Voce digitou o numero {n}')