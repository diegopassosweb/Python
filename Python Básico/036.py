

casa = float(input("Valor da casa: R$"))
salario = float(input("Salario do comprador: R$"))
anos = int(input("Anos de financiamento? "))
prest = casa / (anos * 12)
min = salario * 30 / 100
print(f'Para pagar uma casa de R$ {casa:.2f} em {anos} anos', end=' ')
print(f'A prestaçào sera de R$ {prest:.2f}')
if prest <= min:
    print('Emprestimo pode ser CONCEDIDO!')
else:
    print('Emprestimo NEGADO!')