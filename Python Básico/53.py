
frase = str(input('Digite uma frase: ')).strip().upper()
pl = frase.split()
jun = ''.join(pl)
inv = jun[::-1]
# for letra in range(len(jun) -1, -1, -1):
#     inv += jun[letra]
if inv == jun:
    print('Temos uma palindromo!')
else:
    print('Nao temos um palindromo!')