nome = str(input('Qual o seu nome? '))
if nome == 'User':
    print(f'Ola {nome}')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print(f'Seu nome é muito popular!')
elif nome == 'Ana' or nome == 'Jessica' or nome == 'Julia':
    print(f'Seu nome é muito bonito!')
else:
    print(f'Tenha um bom trabalho!')
print(f'Até mais tarde {nome}')