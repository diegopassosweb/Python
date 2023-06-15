
n1 = int(input("Digite um numero: "))
n2 = int(input("Digite outro numero: "))
n3 = int(input("Digite mais um numero: "))
if n1 < n2 + n3 and n2 < n1 + n3 and n3 < n1 + n2:
    print('Os segmentos acima PODEM formar triangulo:', end=" ")
    if n1 == n2 == n3:
        print('EQUILATERO')
    elif n1 != n2 != n3 != n1:
        print('ESCALENO')
    else:
        print('ISOSCELES')
        
else:
    print('Os segmentos acima NAO podem formar triangulo')