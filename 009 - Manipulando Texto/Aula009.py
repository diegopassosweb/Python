frase = 'Curso em Video Python'
frase =  frase.replace('Python', 'Android')
print(frase)
print(('Cria a frase separada: '),frase.split())
dividido = frase.split()
print(('Mostra a primeira string da frase dividido: '),dividido[0])
print('Pegue a segunda string e mostre a terceira letra: ', dividido[2][3])
print('Coloca o "Video" em minisucula e retorna seu local', frase.lower().find('video'))
print(('"Curso" esta em que posiçao?'),(frase.find('Curso')))
print(('"Curso" esta na frase? True ou False: '),'Curso' in frase)
print(('Mostra a primeira letra: '),frase[0])
print(('Troca python por android: '),frase.replace('Python', 'Android'))
print(('Mostra o tamanho da frase,'), len(frase), "letras + espaços")
print(('Remove os espaços indesejados antes e depois'), (frase.strip()))
print('Coloca a frase toda em MAIUSCULA e conta quantas vezes tem o "O"', (frase.upper().count('O')))
print(('A frase tem '),frase.count('o'), ('letras "o"'))
print(('A quarta letra é: '), frase[3])
print(('Decima terceira letra até o final: '), frase[13:])
print(('Da quarta letra até a decima segunda: '), frase[3:13])
print(('Da letra um até a quinze pulando de dois em dois: '),frase[1:15:2])
print(('Pulando de dois em dois sem saber inicio e fim: '), frase[::2])