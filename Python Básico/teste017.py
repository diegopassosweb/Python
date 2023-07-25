
itens = ['lanche', 'suco', 'hamburguer', 'pizza', 'sorvete']

itens.insert(0, 'cachorro quente') # adiciona na posiçao determinada
itens.append('doce') # adiciona no final

del itens[3] # delete o elemento determinado
itens.pop(3) # delete o elemento determinado
if 'pizza' in itens:
    itens.remove('pizza')
itens.pop() # remove o ultimo elemento
itens.remove('cachorro quente') # delete um elemento pelo nome

print(itens)

valores = [8,4,5,2,1,5,7,3]
valores.sort() # coloca em ordem
valores.sort(reverse=True) # coloca em ordem reversa
len(valores)
valores[2] = 10
print(valores)

a = [2, 3, 4 ,7]
b = a[:]
b[2] = 8
print(a)
print(b)

