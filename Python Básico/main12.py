
nome = str(input("Digite seu nome: ")).strip()
if nome == 'user':
    print(f'Bom dia {nome}')
elif nome == 'PEDRO' or nome == 'MARIA' or nome == 'PAULO':
    print('Seu nome é popoular no Brasil')
else:
    print(f'Volte sempre {nome}')
print(f'Até logo {nome}')