#023: Faça um programa que leia um número de 0 a 9999
# e mostre na tela cada um dos dígitos separados.

num = int(input("Informe um numero: "))
u = num // 1 & 10#divisao inteira por 1 e tire o resto da divisao por 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print(f'Analisando o numero: {num}')
print(f'Unidade: {u}')
print(f'Dezena: {d}')
print(f'Centena: {c}')
print(f'Milhar: {m}')

#print(f'Analisando o numero: {num}')
#print(f'Unidade: {n[3]}')
#print(f'Dezena: {n[2]}')
#print(f'Centena: {n[1]}')
#print(f'Milhar: {n[0]}')