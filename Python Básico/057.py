

sexo = str(input('Informe seu sexo: [M/F] ')).upper()[0].strip()
while sexo not in 'MmFf':
    sexo = str(input('Dados invalidos, Por favor, informe seu sexo: [M/F] ')).upper()[0].strip()
print(f'Sexo {sexo} registrado com sucesso!')