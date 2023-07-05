try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a/b
except (ValueError, TypeError):
    print(f'Erro tipo de dados')
except ZeroDivisionError:
    print('Erro divisao por 0')
except KeyboardInterrupt:
    print('Nao informou dados')
except Exception as erro:
    print(f'Erro de {erro.__class__}')
else:
    print(f'O resultado é {r:.1f}')
finally:
    print('Fim!')
    