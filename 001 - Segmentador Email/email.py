# email que vai usar
#divide o email com o @, a primeira parte usa o nome e a segunda vai ter o dominio salvo
# separa o dominio .

def main():
    print("Bem vindo ao separador de Email")
    print("")
    
    email_input = input("Digite seu email: ")
    
    (username, domain) = email_input.split("@")
    (domain, extension) = domain.split(".")
    
    print("Username : ", username)
    print("Dominio :", domain)
    print("Extensão: ", extension)

while True:
    main()