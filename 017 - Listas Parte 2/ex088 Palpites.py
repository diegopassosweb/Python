from random import randint
lista = list()
sorteio = list()
print("-="*30)
q = int(input("Quantos sorteios? "))
tot = 1
while tot <= q:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    sorteio.append(lista[:])
    lista.clear()
    tot += 1
print(f'Os numeros sorteados foram {sorteio}')
