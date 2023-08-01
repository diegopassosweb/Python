
def ajuda(com):
    help(com)
    
def title(msg, cor=0):
    tam = len(msg) + 4
    print('-'* tam)
    print(msg)
    print('-'*tam)
    
    
comando = ''
while True:
    title('SISTEMA DE AJUDA')
    comando = str(input('Funçao ou Biblioteca > '))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)