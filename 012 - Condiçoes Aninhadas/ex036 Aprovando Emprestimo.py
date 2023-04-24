casa = float(input('Valor da casa: R$'))
salario = float(input('Salario do comprador: R$'))
anos = int(input('Quantos anos de financiamento? '))
prestaçao = casa / (anos * 12)
min = salario * 30 / 100
print(f'Para pagar uma casa de R% {casa} em {anos} anos', end="")
print(f' A prestaçao sera de R$ {prestaçao}')
if prestaçao <= min:
    print(f'Emprestimo pode ser CONCEDIDO!')
else:
    print(f'Emprestimo NEGADO!')

