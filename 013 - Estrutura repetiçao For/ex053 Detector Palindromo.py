frase = str(input('Digite uma frase: ')).strip().upper() #tira espaços e deixa maiuscula
palavra = frase.split() #separou a frase em uma lista
junto = "".join(palavra) # juntou a frase
inverso = "" 
inverso = junto[::-1]
'''for letra in range(len(junto) -1, -1, -1): #seu inverso
    inverso += junto[letra]'''
print(f'O inverno de {junto} é {inverso}')
if inverso == junto:
    print('A frase digitada é um palindromo')
else:
    print('A frase náo é um palindromo')

