n1 = int(input('Primeiro segmento: '))
n2 = int(input('Segundo segmento: '))
n3 = int(input('Terceiro segmento: '))
if n1 < n2 + n3 and n2 < n1 + n3 and n3 < n1 + n2:
    print('Podem formar Triangulo!')
    if n1 == n2 == n3:
        print('EQUILATERO!')
    elif n1 != n2 != n3 != n1:
        print('ESCALENO!')
    else:
        print('ISOSCELES')
else:
    print('Não podem formar triangulo!')