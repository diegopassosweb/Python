s = str(input('Informe seu sexo: [M/F] ')).strip().upper()[0]

while s not in "MmFf":
    s = str(input('Dados invalidos. Por favor, informe novamente'))
print(f'{s} Registrado com sucesso!')
    