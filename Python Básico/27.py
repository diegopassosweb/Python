n = str(input('Seu nome completo é: ')).strip()
nome = n.split()
print(f'Seu primeiro nome é {nome[0]}')
print(f'Seu ultimo nome é {nome[len(nome) -1]}')