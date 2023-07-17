from datetime import date
atual = date.today().year
nasc = int(input('Ano de nascimento: '))
idade = atual - nasc
print(f'Quem nasceu em {nasc} tem {idade} anos em {atual}')
if idade == 18:
    print('Se aliste imediatamente!')
elif idade < 18:
    saldo = 18 - idade
    anos = atual + saldo
    print(f'Faltam {saldo} anos para se alistar')
    print(f'Seu alistamento sera em {anos}')
elif idade > 18:
    saldo = idade - 18
    anos = atual - saldo
    print(f'Ja deveria ter se alistado ha {saldo} anos')
    print(f'Seu alistamento foi em {anos} ')