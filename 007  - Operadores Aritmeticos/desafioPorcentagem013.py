salario = float(input('Digite o seu salario: '))
novo = salario + (salario * 15 / 100)
print(f'Um funcionario que ganhava R${novo:.2f}, com aumento de 15%, passa a receber {salario:.2f}')
