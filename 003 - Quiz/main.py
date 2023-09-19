import re
import csv

lista_valid_email = []
lista_invalid_email = []

def verificador_de_e_mail(email):
    if re.search(r'\b[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}\b', email):
        lista_valid_email.append(email)
    else:
        lista_invalid_email.append(email)
        
ficheiro = './dados.csv'

emails = []

with open(ficheiro) as file:
    ler_csv = csv.reader(file)
    for row in ler_csv:
        verificador_de_e_mail(row[2])
        emails.append(row[2])

print('E-m,ails validos:')
for email in lista_valid_email:
    print(email)

print('\nE-mails invalidos:')
for email in lista_invalid_email:
    print(email)
    
