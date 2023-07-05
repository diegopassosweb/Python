
def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31m[ERRO] Digite um numero inteiro valido \033\m')
            continue
        except (KeyboardInterrupt):
            print('\n\033[31mInterrompido pelo usuario!\033[m')
            return 0
        else:
            return n
        
def leiafloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO: digite um numero real valido \033[m')
            continue
        except (KeyboardInterrupt):
            print('\n\033[31mUsuario nao digitiu um numero \033[m')
            return 0
        else:
            return n