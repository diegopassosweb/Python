palavras = ('pastel', 'sabonete', 'panela', 'piada', 'pernambuco', 'cachorro', 'tabuada', 'paraguai', 'esquecido')

for p in palavras:
    print(f'\nNa palavra {p.upper()} temos ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')