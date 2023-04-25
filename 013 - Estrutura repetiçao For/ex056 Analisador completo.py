somaid = 0
mediaid = 0
maiorh = 0
nomev = ''
totm = 0
for p in range(1, 5):
    print(f'-------- {p} PESSOA --------')
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    somaid += idade
    if p == 1:
        maiorh = idade
        nomev = nome
        
    if sexo in "Mm" and idade > maiorh:
        maiorh = idade
        nomev = nome
    if sexo in "Ff" and idade < 20:
        totm += 1
mediaid = somaid / 4
print(f'A media de idade do grupo é de {mediaid}')
print(f'O homem mais velho tem {maiorh} anos e se chama {nomev}')
print(f'Ao todo sao {totm} mulheres com menos de 20 anos')
