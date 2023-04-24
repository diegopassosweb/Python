n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
m = (n1 + n2) / 2
print(f'Tirando {n1} e {n2}, a media do aluno é {m}')
if m >= 5 and m < 6:
    print('O aluno esta em RECUPERAÇÃO')
elif m < 5:
    print('O aluno esta REPROVADO')
elif m >= 7:
    print('O aluno esta APROVADO')