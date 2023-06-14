vel = float(input("Velocidade do carro? "))
if vel > 80:
    print('Multado! Voce excedeu o limite de velocidade!')
    m = (vel - 80) * 7
    print(f'Voce deve pagar uma multa de {m:.2f}')
print('Tenha um bom dia! Dirija com segurança')