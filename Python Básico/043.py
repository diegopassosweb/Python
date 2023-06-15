
peso = float(input("Qual é o seu peso? KG "))
altura = float(input("Qual é a sua altura? (M) "))
imc = peso / (altura ** 2)
print(f'O IMC dessa pesoa é de {imc:.1f}')
if imc < 18.5:
    print('Voce esta ABAIXO do peso normal')
elif 18.5 <= imc < 25:
    print('Parabens, voce esta na faixa de peso NORMAL')
elif 25 <= imc < 30:
    print('Voce esta em SOBREPESO')
elif imc >= 40:
    print('Voce esta em OBESIDADE MORBIDA')