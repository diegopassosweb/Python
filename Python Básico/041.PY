from datetime import date
atual = date.today().year
nasc = int(input("Ano de nasc: "))
idade = atual - nasc
print(f'O atleta tem {idade} anos')
if idade <= 9:
    print('Atleta mirim')
elif idade <= 14:
    print('Atleta infantil')
elif idade <= 19:
    print('Atleta Junior')
elif idade <= 25:
    print('Atleta Senior')
else:
    print('Atleta Master') 
    
    