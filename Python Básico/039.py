from datetime import date
atual = date.today().year

nasc = int(input("Digite o ano de nasc: "))
idade = atual - nasc
print(f'Quem nasceu em {nasc} tem {idade} anos em {atual}')
if idade == 18:
    print('Se aliste imediatamente!')
elif idade < 18:
    saldo = 18 - idade
    print(f'Aguarde ter 18 anos para o alistamento, faltam {saldo}')
    ano = atual + saldo
    print(f'Seu alistamento sera em {ano} ano')
elif idade > 18:
    saldo = idade - 18
    ano = atual - saldo
    print(f'Voce ja deveria ter se alistado ha {saldo} anos')
    print(f'Seu alistamento foi em {ano}')


