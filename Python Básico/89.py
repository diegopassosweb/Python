ficha = list()
while True:
    
    nome = str(input('Nome: '))
    n1 = float(input('Nota 1: '))
    n2 = float(input('Nota 2: '))
    m = (n1 + n2) / 2
    ficha.append([nome, [n1, n2], m])
    r = str(input('Quer continuar? [S/N] '))
    if r in 'Nn':
        break
print(f'{"No.":<4}{"NOME":<10}{"MEDIA":>8}')
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print('-' * 35)
    opc = int(input('Mostrar notas de qual aluno? 999 parar: '))
    if opc == 999:
        break
    if opc <= len(ficha) -1:
        print(f'Notas de {ficha[opc][0]} sao {ficha[opc][1]}')