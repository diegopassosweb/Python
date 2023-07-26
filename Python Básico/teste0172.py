galera = [['Joao',19], ['Maria',22], ['Pedro', 32], ['Joaquin',40]]
for p in galera:
    print(f'{p[0]} tem {p[1]} anos de idade')

print()    
galera2 = list()
dado = list()
totmai = totmen = 0
for c in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera2.append(dado[:])
    dado.clear()
for d in galera2:
    if d[1] >= 21:
        print(f'{d[0]} é maior de idade')
        totmai +=1
    else:
        print(f'{d[0]} é menor de idade')
        totmen +=1
print(f'Temos {totmai} maiores e {totmen} menores')