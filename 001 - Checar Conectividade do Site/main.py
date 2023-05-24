# import urllib
# use urllib.request para pegar os dados da url
# escreva uma função que pega a url
# retorne uma resposta

import urllib.request as urllib

def main(url):
    print("Verificando a conectivisdade ")
    
    response = urllib.urlopen(url)
    print("Conectado", url, "com sucesso")
    print("A resposta do codigo foi:" , response.getcode())

print("Checando a conectividade do site")
input_url = input("Digite a url do seu que quer verificar: ")

main(input_url)