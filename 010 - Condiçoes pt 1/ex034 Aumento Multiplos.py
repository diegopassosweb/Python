s = float(input('Qual é o salario do funcionario? '))
if s <= 1250:
    n = s + (s * 15 / 100)
else:
    n = s + (s * 10 / 100)
print(f'Quem ganhava R${s:.2f} passa a ganhar R${n:.2f}')