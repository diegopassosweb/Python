casa = float(input('Valor da casa R$: '))
sal = float(input('Salario R$: '))
anos = float(input('Quantos anos de emprestimo: '))
prest = casa / (anos * 12)
minimo = sal * 30 / 100
print(f'Para pagar uma casa de R${casa:.2f} em {anos} anos', end='')
print(f' a prestação sera de R${prest:.2f}')
if minimo <= prest:
    print(f'Emprestimo Concedido!')
else:
    print(f'Emprestimo NEGADO!')