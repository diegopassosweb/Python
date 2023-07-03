
def par(n=0):
    if n % 2 == 0:
        return True
    else:
        return False

n = int(input('Digite um numero: '))
if par(n):
    print('É PAR')
else:
    print('Não É PAR')