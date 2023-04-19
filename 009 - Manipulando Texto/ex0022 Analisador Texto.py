#022: Crie um programa que leia o nome completo de uma pessoa e mostre:
# - O nome com todas as letras maiúsculas e minúsculas. - 
# Quantas letras ao todo (sem considerar espaços). - 
nome = str(input('Digite seu nome completo: ')).strip()
(print('Carregando seu nome...'))
print(f'Seu nome em MAIUSCULAS é: {nome.upper()}')
print(f'Seu nome em minusculas é: {nome.lower()}')
letras = len(nome) - nome.count(' ')
print(f'Seu nome tem: {letras} letras;')
print(f'Seu primeiro nome tem {nome.find(" ")}, letras')
separa = nome.split()
print(f'Seu primeiro nome é {separa[0]}, e tem {len(separa[0])}, letras')