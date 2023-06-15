
n1 = float(input("Primeira nota: "))
n2 = float(input("Segunda nota: "))
media = (n1 + n2) / 2
print(f'A media do aluno é {media:.1f}')
if media >= 5 and media < 7:
    print('O aluno esta em RECUPERAÇÃO')
elif media < 5:
    print('O aluno esta REPROVADO')
else:
    print('O aluno esta APROVADO')
    