soma = 0
media = 0
maioridadehomem = 0
nomevelho = 0
totmulher20 = 0
for c in range(1, 5):
    print(f' {c} PESSOA')
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('[M/F]: ')).strip()
    soma += idade
    if c == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher20 += 1
media = soma / c
print(f'A media de idade do grupo é de {media} anos')
print(f'O homem mais velho tem {maioridadehomem} anos e se chama {nomevelho}')
print(f'Ao todo são {totmulher20} mulheres com menos de 20 anos')