
frase = str(input('Digite uma frase: ')).strip().upper()
print(f'A letra [A] aparece {frase.count("A")} vezes')
print(f'A primeira letra [A] apareceu na posiçao {frase.find("A")+1}')
print(f'A ultima letra [A] apareceu na posiçao {frase.rfind("A")+1}')