valores = list()
for cont in range(0,5):
    valores.append(int(input('Digite um valor: ')))
#valores.append(5)
#valores.append(9)
#valores.append(4)

for c,v in enumerate(valores):
    print(f' Na posiçao {c} encontrei o valor {v}...', end="")