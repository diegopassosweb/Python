cont = 'S'
media = 0
soma = 0
quant = 0
maior = 0
menor = 0
while cont in 'Ss':
    n = int(input('Digite um numero: '))
    soma += n
    quant += 1
    if quant == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    cont = str(input('Quer continuar? [S/N] ')).upper().strip()
media = soma / quant
print(f'Voce digitou {quant} numeros e a media foi {media}')
print(f'O maior valor foi {maior} e o menor foi {menor}')