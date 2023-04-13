#nome = input('Qual o seu nome? ')
#print(f'Prazer em te conhecer {nome:=^20}!')

# Para ficar na mesma linha adicione no final end=' '
# Para quebrar na mesma linha \n

n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print(f'A soma é {s}, \n o produto é {m} e a divisao é (3 casas decimais flutuantes) {d:.3f}', end=' ')
print(f'A divisao inteira é {di} e potencia, raiz quadrada {e}')