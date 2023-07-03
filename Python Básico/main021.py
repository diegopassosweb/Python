
def contador(i, f, p=0 ):
    '''
    i inicio da contagem
    p passo da contagem
    f fim da contagem
    '''
    c = i
    while c<= f:
        print(f'{c}', end='..')
        c += p
    print('fim')

contador(2, 10,2)

