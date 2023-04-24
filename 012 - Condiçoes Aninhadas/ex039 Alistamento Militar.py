from datetime import date
atual = date.today().year
nasc = int(input('Ano de nascimento: '))
idade = atual - nasc
print(f'Quem nasceu em {nasc} tem {idade} anos em {atual}')
if idade == 18:
    print('Voce tem que se alistar imediatamente!')
elif idade < 18:
    saldo = 18 - idade
    print(f'Faltam {saldo} anos para o alistamento')
    ano = atual + saldo
    print(f'Seu alismento sera em {ano}')
elif idade > 18:
    saldo = idade - 18
    ano = atual - saldo
    print(f'Voce ja deveria ter se alistado ha {saldo} anos')
    print(f'Seu alistamento foi em {ano}')