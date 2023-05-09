def somar(a=0,b=0,c=0):
    '''
    => Faz a soma de tres valores e mostra o resultado na tela.
    :param a: o primeiro valor
    :param b: o segundo valor
    :param c: o terceiro valor
    '''
    s = a + b + c
    print(f'A soma do vale é {s}', end="\n")
    
somar(3,2,5)
somar(8,4)
somar(c=3,a=2,b=9)
help(print)