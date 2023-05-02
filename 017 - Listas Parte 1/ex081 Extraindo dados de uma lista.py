valores = []
while True:
    valores.append(int(input("Digite um valor: ")))
    resp = str(input("Quer continuar? [S/N] "))
    if resp in "Nn":
        break
print("-="*40)
print(f'Voce digitou {len(valores)} elementos')
valores.sort(reverse=True)
print(f'Os valores em ordem sao {valores}')
if 5 in valores:
    print('Valor 5 faz parte da lista!')
else:
    print('O valor 5 nao foi encontrado!')