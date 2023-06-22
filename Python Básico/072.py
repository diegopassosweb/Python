count = ('zero', 'um', 'dois', 'tres', 'quatro',
         'cinco', 'seis', 'sete', 'oito', 'nove',
         'dez', 'onze', 'doze', 'treze', 'catorze',
         'quinze', 'dezesseis', 'dezessete', 'dezoito',
         'dezenove', 'vinte')
while True:
    n = int(input('Digite um numero entre 0 e 20: '))
    mais = str(input('Quer continuar? [S/N] ')).upper()[0].strip()
    if 0 <= n <= 20:
        break
print(f'Voce digitou o numero {count[n]}')


