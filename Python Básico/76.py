listagem = ('Lapis', 1.75,
            'Borracha', 2,
            'Caderno', 15.99,
            'Estojo', 25,
            'Compasso', 4.99,
            'Mochila', 50.99,
            'Canetas', 25.99,
            'Livro', 19.90)
for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}', end='')
    else:
        print(f'R${listagem[pos]:>7.2f}')
