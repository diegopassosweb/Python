# ( tupla ), [ lista ], { dicionario }

lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim')
# tuplas sao imutaveis

# for pos, comida in lanche:
#     print(f'Eu vou comer {comida} na posição {pos}')

for cont in range(0, len(lanche)):
    print(f'Euvou comer {lanche[cont]} na posicão {cont}')
    
# print(sorted(lanche)) coloca em ordem
print('Comi demais!')

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
print(f'A tupla tem {len(c)} posiçoes')
print(f'O numero 5 aparece {c.count(5)} vezes') # quantas vezes aparece o numero 5
print(f'O numero 8 esta na posiçao {c.index(8)}')

pessoa = ('Gustavo', 39, 'M', 99.88)
print(pessoa)
del(pessoa)
