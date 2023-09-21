import random
import string

def criar_senha():
    alf_menos = string.ascii_lowercase
    alf_mais = string.ascii_uppercase
    numeros = '123456789'
    simbolos = '[]{}()*;/,_-'

    combinar = alf_mais
    combinar = combinar + alf_menos
    combinar = combinar + numeros
    combinar = combinar + simbolos

    comprimento = 10

    senha = "".join(random.sample(combinar, comprimento))

    print(senha)

criar_senha()
