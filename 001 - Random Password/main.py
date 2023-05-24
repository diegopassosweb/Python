# pergunte se quer gerar a senha
# se sim verificar o tamanho da senha
# gerar a senha
# print


import string
import random

characters =list(string.ascii_letters + string.digits + "!@#$%^&*()")

def generate_password():
    password_length = int(input("Quantos caracteres para sua senha? "))
    
    random.shuffle(characters)
    
    password = []
    
    for x in range(password_length):
        password.append(random.choice(characters))
        
    random.shuffle(password)
    
    password = "".join(password)
    
    print(password)

option = input("Voce quer gerar a senha? (Sim/Não): ")

if option == "Sim":
    generate_password()
elif option == "Não":
    print("Fim")
    quit()
else:
    print("Valor invalido")
    quit()

