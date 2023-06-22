lanche = ('Hamburguer', 'pizza', 'suco', 'Pudim')
# print(len(lanche))
print(sorted(lanche))
print(lanche)
for comida in lanche:
    print(f'Vou comer {comida}')

for cont in range(0, len(lanche)):
    print(f'{lanche[cont]} na posiçao {cont}')
    
for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posiçao {pos}')
print('Estou cheio')