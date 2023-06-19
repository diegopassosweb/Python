
f = str(input('Digite uma frase: ')).strip().upper()
p = f.split()
j = ''.join(p)
i = ''
i = j[::-1]
'''for letra in range(len(j) -1, -1, -1):
    i += j[letra]'''
print(f'O inverso de {j} é {i}')
if i == j:
        print('Temos um palindromo!')
else:
        print('A frase digitada nao é um palindromo')
    # print(f'Voce digitou a frase {j}')