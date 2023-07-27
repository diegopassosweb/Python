
pessoa = dict()
galera = list()
soma = media = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo: [M/F] ')).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('Erro M ou F')
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    galera.append(pessoa.copy())
    while True:
        r = str(input('Continua? [S/N] ')).upper()[0]
        if r in 'SN':
            break
        print('ERRO S ou N')
    if r == 'N':
        break
print(f'Ao todo temos {len(galera)} pessoas cadastradas')
media = soma / len(galera)
print(f'A media de idade é de {media:5.2f} anos')
print(f'As mulheres cadastradas foram ', end='')
for p in galera:
    if p['sexo'] in 'Ff':
        print(f' {p["nome"]} ', end='')
print()
print(f'A listagem das pessoas acima da media: ')
for p in galera:
    if p['idade'] >= media:
        print('  ')
        for k, v in p.items():
            print(f' {k} = {v} ', end='')
        print()
        