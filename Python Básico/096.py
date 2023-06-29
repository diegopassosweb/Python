
def area(l, c):
    a = l * c
    print(f'A area de um terreno com a {l} x {c} é de {a}m²' )
    
print(' Controle de terrenos')
print('-'*20)
l = float(input('Largura (m): '))
c = float(input('Comprimento (m): '))
area(l, c)
    