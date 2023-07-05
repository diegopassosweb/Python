from uteis import dado, arquivo
from time import sleep

arq = 'arquivo.txt'
if not arquivo.arquivoExiste(arq):
    arquivo.criarArquivo(arq)

while True:
    resp = dado.menu({'Ver Cadastro', 'Cadastrar', 'Sair', })
    if resp == 1:
        # dado.cabeçalho('Opção 1')
        dado.lerArquivo(arq)
    elif resp == 2:
        dado.cabeçalho('Opção 2')
    elif resp == 3:
        dado.cabeçalho('Fim')
        break
    else:
        print('\033[31m[ERRO] Digite uma opçao valida\033[m')
    sleep(2)
