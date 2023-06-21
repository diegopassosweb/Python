n = 0
while True:
    n = int(input('Digite um numero para sua tabuada (999 para parar): '))
    if n == 999 or n < 0:
        break
    for c in range(1, 11):
        print(f'{n} x {n} = {n*c}')
print('Tabuada encerrada!')