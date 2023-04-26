n = cont = soma = 0
n = int(input('Digite um numero: [999 para parar] '))
while n != 999:
    soma += n
    cont += 1
    n = int(input('Digite um numero: [999 para parar] '))
print(f'Voce digitou {cont} numeros e a soma foi {soma}')