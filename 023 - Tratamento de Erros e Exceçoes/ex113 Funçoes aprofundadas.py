def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO: digite um numero inteiro \033[m')
            continue
        except (KeyboardInterrupt):
            print('\n\033[31mEntrada de dados interrompida pelo usuario\033[m')
            return 0
        else:
            return n
        
        
def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO: digite um numero inteiro \033[m')
            continue
        except (KeyboardInterrupt):
            print('\n\033[31mEntrada de dados interrompida pelo usuario\033[m')
            return 0
        else:
            return n
        
num = leiaint('Digite um valor: ')
num2 = leiaFloat('Digite um real: ')
print(f'O valor digitado foi {num}')
print(f'O valor inteiro digitado foi {num2}')