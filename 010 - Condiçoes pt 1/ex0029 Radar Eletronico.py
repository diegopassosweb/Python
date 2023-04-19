vel = float(input('Qual a velocidade atual do carro? '))
if vel > 80:
    print('Cuidado, voce passou do limite de velocidade!')
    m = (vel - 80) * 7
    print(f'Voce recebeu uma multa! de {m}')
print(f'Tenha um Bom dia!')