peso = float(input('Qual é o seu peso? (Kg)'))
altura = float(input('Qual a sua altura? (m)'))
imc = peso / (altura ** 2) # peso pela altura ao quadrado
print(f'O IMC dessa pessoa é de {imc:.1f}')
if imc < 18.5:
    print('Voce esta ABAIXO do peso normal')
elif imc >= 18.5 and imc < 25:
    print('PARABENS, voce esta na faixa do peso NORMAL')
elif 25 <= imc < 30:
    print('Voce esta em SOBREPESO')
elif 30 <= imc < 40:
    print('Voce esta em OBESIDADE, cuidado!')
elif imc >= 40:
    print('Voce esta em OBESIDADE MORBIDA!')