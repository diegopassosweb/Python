d = int(input('Quantos dias foi alugado? '))
km = float(input('Quantos Km rodados? Km '))
pago = (d * 60) + (km * 0.15)
print(f'O total a pagar é de R${pago:.2f}')