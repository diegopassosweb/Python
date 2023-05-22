# defina as funçoes que precisa
# print as opçoes para usar
# pergunte quais valores
# chame as funçoes
# loop para continuar sair

def add(a, b):
    answer = a + b
    print(str(a) + " + " + str(b) + " = " + str(answer) + "\n")

def sub(a, b):
    answer = a - b
    print(str(a) + " - " + str(b) + " = " + str(answer)  + "\n")

def mul(a, b):
    answer = a * b
    print(str(a) + " * " + str(b) + " = " + str(answer) + "\n")
    
def div(a , b):
    answer = a / b
    print(str(a) + " / " + str(b) + " = " + str(answer) + "\n")

while True:
    print('A. adição')
    print('B. Subtração')
    print('C. Multiplicaçao')
    print('D. Divisao')
    print('E. Exit')

    choice = input('Escolha uma opçao: ')

    if choice == "a" or choice == "A":
        print('Adição')
        a = int(input('Digite um numero: '))
        b = int(input('Digite outro numero: '))
        add(a, b)
    elif choice == "b" or choice == "B":
        print('Subtração')
        a = int(input('Digite um numero: '))
        b = int(input('Digite outro numero: '))
        sub(a, b)
    elif choice == "d" or choice == "D":
        print('Divisão')
        a = int(input('Digite um numero: '))
        b = int(input('Digite outro numero: '))
        div(a, b)
    elif choice == "e" or choice == "E":
        print('Fim')
        quit()