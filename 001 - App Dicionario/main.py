import math

def area_quadrado(lado):
    return lado ** 2

def area_retangulo(base, altura):
    return base * altura

def area_triangulo(base, altura):
    return (base * altura) / 2

def area_circulo(raio):
    return math.pi * (raio ** 2)

def calculadora_geometrica():
    print("Bem-vindo(a) à calculadora de figuras geométricas!")
    print("Qual figura você gostaria de calcular a área?")
    print("1. Quadrado")
    print("2. Retângulo")
    print("3. Triângulo")
    print("4. Círculo")
    escolha = input("Digite o número correspondente à figura: ")
    if escolha == '1':
        lado = float(input('Digite o tamanho do lado do quadrado: '))
        print(f'A area do quadrado é de {area_quadrado(lado)}')
    elif escolha == '2':
        base = float(input('Digite o tamanho da base do retangulo: '))
        altura = float(input('Digite o tamanho da altura do retangulo: '))
        print(f'A area do retangulo é {area_retangulo(base, altura)}')
    elif escolha == '3':
        base = float(input('Digite o tamanho da base do triangulo: '))
        altura = float(input('Digite o tamanho da altura do triangulo: '))
        print(f'A area do triangulo é {area_triangulo(base, altura)}')
    elif escolha == '4':
        raio = float(input('Digite o tamanho do raio do circulo: '))
        print(f'A area do circulo é de {area_circulo(raio)}')
    else:
        print('Opçao invalida')

calculadora_geometrica()