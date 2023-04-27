
while True:
    n = int(input('Digite o valor da tabuada: '))
    if n < 0:
        break
    print('-' * 30)
    for c in range(1,11):
        print(f' {n} x {c} = {n*c}')
    print('-' * 30)
print('Fim!')