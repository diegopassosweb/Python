listanum = []
mai = 0
men = 0

for c in range (0, 5):
    listanum.append(int(input(f'Digite um valor para a Posição {c}: ')))
    if mai == 0:
        mai = men = listanum[c]
    else:
        if listanum[c] > mai:
            mai = listanum[c]
        if listanum[c] < men:
            men = listanum[c]
    
    
print(f'Voce digitou os valores {listanum}')
print(f'O maior valor digitado foi {mai}',)
for i, v in enumerate(listanum):
    if v == mai:
        print(f' posiçao {i}...', end='')
print()
print(f'O menor valor digitado foi {men}')
for i, v in enumerate(listanum):
    if v == men:
        print(f' posiçao {i}...', end='')
print()