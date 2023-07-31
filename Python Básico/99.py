from time import sleep
def maior(*num):
    cont = maior = 0
    print('\nAnalisando os valores...')
    
    for valor in num:
        print(f'{valor} ', end='', flush=True)
        sleep(0.2)
    if cont == 0:
        maior = valor
    else:
       if valor > maior:
            maior = valor
    cont += 1
    print(f'Foram informados {cont} valores')
    print(f'O maior valor foi {maior}')    
maior(2,5,10)