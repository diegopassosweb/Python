
vel = int(input('Qual é a velocidade atual do carro? '))
if vel > 80:
    print('Multado! Excedeu o limite de 80Km/h')
    mult = (vel - 80) * 7
    print(f'Voce deve pagar uma multa de R${mult:.2f}')
print('Dirija com segurança!')