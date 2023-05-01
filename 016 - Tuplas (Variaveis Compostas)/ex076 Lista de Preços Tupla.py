listagem = ("Lápis", 1.85,
            "Borracha", 2,
            "Caderno", 12.22,
            "Estojo", 5.45,
            "Transferidor", 4.50,
            "Caneta", 2,
            "Mochila", 120.32,
            "Livro", 15.23)
for pos in range(0, len(listagem)):
    if pos  % 2 == 0:
        print(f' {listagem[pos]:.<30}', end="")
    else:
        print(f'R${listagem[pos]:>7.2f}')
