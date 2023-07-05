from uteis import dado

def arquivoExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True

def criarArquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('ERRO ao criar arquivo')
    else:
        print(f'Arquivo {nome} criado com sucesso')
        
def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('Erro ao ler arquivo')
    else:
        dado.cabeçalho('PESSOAS CADASTRADAS')
        print(a.read())