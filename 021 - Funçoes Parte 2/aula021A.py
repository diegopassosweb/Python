#print(input.__doc__)
#help(input)

def contador(i,f,p):
    '''
    => Faz uma contagem e mostra na tela.
    :param i: inicio de contagem
    :param f: fim da contagem
    :parem p: passo da contagem
    :return: sem retorno
    '''
    c = i
    while c <= f:
        print(f'{c}', end=" ")
        c+=p
    print('FIM!')

contador(0,100,10)

help(contador)