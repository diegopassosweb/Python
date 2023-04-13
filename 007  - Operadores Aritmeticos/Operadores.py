n1 = int(input('Digite um numero: '))
n2 = int(input('Digite outro numero: '))

soma = n1 + n2
sub = n1 - n2
mult = n1 * n2
div = n1 / n2
pot = n1 ** n2
divint = n1 // n2
mod = n1 % n2

# Ordem de Precedencia 
# 1 ()
# 2 **
# 3 * / // e %
# 4 + e -

print(f'A soma de {n1} + {n2} = {soma}')
print(f'A subtração de {n1} - {n2} = {sub}')
print(f'A multiplicação de {n1} * {n2} = {mult}')
print(f'A divisão de {n1} / {n2} = {div}')
print(f'A potencia, raiz quadrada faça n1 ** n1 (1/2) {n1} ** {n2} = {pot}')
print(f'A divisao inteira de {n1} // {n2} = {divint}')
print(f'O resto da divisao de {n1} % {n2} = {mod}')
#print('Para adição +')
#print('Para subtração -')
#print('Para multiplicação *')
#print('Para divisão /')
#print('Para potência **')
#print('Para divisão inteira //')
#print('Para modulo ou resto da divisão %')
#print('Recebe é = e comparação sao dois ==')