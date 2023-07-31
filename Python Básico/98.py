from time import sleep

def contador(i,f, p):
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
        
    print(f'Contangem de {i} até {f} de {p} em {p}')
    sleep(1)
    
    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont} ', end='', flush=True)
            sleep(0.5)
            cont += p
    else:
        cont = i
        while cont >= f:
            print(f'{cont} ', end='', flush=True)
            sleep(0.5)
            cont -= p

contador(1, 100, 10)
contador(10, 0, 2)
print('Sua vez')
ini = int(input('Inicio: '))
fim = int(input('Fim: '))
pas = int(input('Passo: '))
contador(ini, fim, pas)