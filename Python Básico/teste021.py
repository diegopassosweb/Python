
def contador(i,f,p):
    '''
    => i inicio
    => f fim
    => p passo
    => c contador
    '''
    c = i
    while c <= f:
        print(f'{c}', end='..')
        c += p
    print('fim')
    
contador(2,10,2)
help(contador)