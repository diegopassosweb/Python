
def aumentar(preco = 0, taxa = 0, format=False):
    res = preco + (preco * taxa / 100)
    return res if format == False else moeda(preco)


def diminuir(preco = 0, taxa= 0, format = False):    
    res = preco - (preco * taxa / 100)
    return res if format is False else moeda(res)
    
    
def dobro(preco= 0, format = False):
    res = preco * 2
    return res if not format else moeda(res)


def metade(preco = 0, format = False):
    res = preco / 2
    return res if not format else moeda(res)

def moeda(preco= 0, moeda= 'R$'):
    return f'{moeda} {preco:.2f}'.replace('.',',')

def resumo(preco = 0, taxaa= 10, taxar = 5):
    print('-' * 30)
    print('RESUMO DO VALOR'.center(30))
    print('-' * 30)
    print(f'Preco analisado: \t{moeda(preco)}')
    print(f'Dobro do preco: \t{dobro(preco, True)}')
    print(f'Meta do preco \t\t{metade(preco, True)}')
    print(f'{taxaa}% de aumento: \t{aumentar(preco, taxaa, True)}')
    print(f'{taxar}% de reduçao: \t{diminuir(preco, taxar, True)}')
    print('-' * 30)
    