n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
media = (n1 + n2) / 2
if media > 7:
    print(f'Tirando {n1} e {n2}, a media do aluno é {media}')
    print('O aluno está APROVADO')
elif media >= 5 and media < 7:
    print(f'Tirando {n1} e {n2}, a media do aluno é {media}')
    print('O aluno esta em RECUPERAÇÃO')
elif media < 5:
    print(f'Tirando {n1} e {n2}, a media do aluno é {media}')
    print('O aluno esta REPROVADO')