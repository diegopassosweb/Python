
def fatorial(n, show = False):
    '''
    => Calcula o Fatorial de um numero
    :param n: O numero a ser calculado.
    :parm show: (opcional) Mostrar ou nao a conta.
    :return: o Valor do Fatoial de um numero n
    '''
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(f' x ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f


print(fatorial(5, show=True))
help(fatorial)