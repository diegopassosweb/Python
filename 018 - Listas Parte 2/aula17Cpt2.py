galera = list()
dado = list()
totma = totme = 0
for c in range(0, 3):
    dado.append(str(input("Nome: ")))
    dado.append(int(input("Idade: ")))
    galera.append(dado[:])
    dado.clear()
for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade')
        totma += 1
    else:
        print(f'{p[0]} é menor de idade')
        totme += 1
print(f" temos {totma} maiores e {totme} menores de idade")