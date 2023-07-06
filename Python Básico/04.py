# n1 = input('Digite um valor: ')
# # print(type(n1))
# print(n1.isnumeric()) # é numero?
# print(n1.isalpha()) # é letra?
# print(n1.isalnum()) # é letra ou numero?
# print(n1.isupper()) # somente letra MAIUSCULAS?
# print(n1.islower()) # somente letra MINUSCULAS?
# print(n1.isispace()) somente espaços? 
# print(n1.istitle()) tem Maiusculas 
valor = input('Digite algo: ')
print(f'O tipo primitivo desse valor é {type(valor)}')
print(f'Só tem espaços? {valor.isspace()}')
print(f'É um numero? {valor.isnumeric()}')
print(f'É alfabetico? {valor.isalpha()}')
print(f'É alfanumerico? {valor.isalnum()}')
print(f'Esta em MAIUSCULAS? {valor.isupper()}')
print(f'Está em minusucas? {valor.lower()}')
print(f'Esta capitalizada? {valor.istitle()}')