r = "S"
s = q = m = maior = menor = 0
while r in "Ss":
    n = int(input('Digite um numero: '))
    s += n
    q += 1
    if q == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    r = str(input('Quer continuar? [S/N]')).upper().strip()[0]
m = s / q

print(f'Voce digitou {q} numeros e a media foi {m:.1f}')
print(f'O menor numero foi {menor} e o maior {maior}')