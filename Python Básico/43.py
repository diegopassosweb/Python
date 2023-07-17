
peso = float(input('Qual é seu peso? (Kg) '))
alt = float(input('Qual é sua altura? (m) '))
imc = peso / (alt ** 2)
if imc <= 18.5:
    print('Abaixo do peso!')
elif imc <= 25:
    print('Peaso ideal!')
elif imc <= 30:
    print('Sobrepeso')
elif imc <= 40:
    print('Obesidade!')
else:
    print('Obesidade morbida!')