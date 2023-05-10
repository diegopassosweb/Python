def aumentar(preco, aumento, show=False):
    preco = preco + (preco * aumento) / 100

    if show:
        return moeda(preco)
    else:
        return preco


def diminuir(preco, reducao, show=False):
    preco = preco - (preco * reducao) / 100

    if show:
        return moeda(preco)
    else:
        return preco


def dobro(preco, show=False):
    preco *= 2

    if show:
        return moeda(preco)
    else:
        return preco


def metade(preco, show=False):
    preco /= 2

    if show:
        return moeda(preco)
    else:
        return preco


def moeda(preco):
    return f'R${preco:.2f}'.replace('.', ',')

def resumo(preco = 0, taxaa=10, taxar=5):
    print('-' * 30)
    print('RESUMO DO VALOR'.center(30))
    print('-' * 30)
    print(f'Preço analisado: \t{moeda(preco)}')
    print(f'Dobro do preço: \t{dobro(preco, True)}')
    print(f'Meta do preço: \t\t{metade(preco, True)}')
    print(f'Com {taxaa}% de aumento: \t{aumentar(preco, taxaa, True)}')
    print(f'Com {taxar}% de reduçao: \t{diminuir(preco, taxar, True)}')
    print('-' * 30)
    
def leiaDinheiro(msg):
    válido = False
    while not válido:
        entrada = str(input(msg)).replace(',', '.').strip()
        if entrada.count('.') == 1 and len(entrada) > 1 and entrada.find('.')!=0 and entrada.replace('.', '0').isnumeric():
            válido = True
            return float(entrada)
        elif entrada.isnumeric():
            válido = True
            return float(entrada)
        else:
            print(f'\033[0;31mERRO: \"{entrada}\" é um preço inválido!\033[m')