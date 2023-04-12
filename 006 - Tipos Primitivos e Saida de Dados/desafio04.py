n = input('Digite um valor: ')

print(f'O tipo primitivo desse valor é {type(n)}')
print(f'So tem espaços? {n.isspace()}')
print(f'É um numero?  {n.isnumeric()}')
print(f'É alfabetico? {n.isalpha()}')
print(f'É alfanumerico? {n.isalnum()}')
print(f'Esta em MAIUSCULAS? {n.isupper()}')
print(f'Esta em minusculas? {n.islower()}')
print(f'Esta capitalizado? {n.istitle()}')

