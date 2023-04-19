#025: Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.
nome = str(input('Qual o seu nome? ')).strip()
print(f'Seu nome possui "Silva?" {"SILVA" in nome.upper()}')