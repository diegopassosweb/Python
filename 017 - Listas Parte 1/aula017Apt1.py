num = [2,5,9,1]
num[2] = 3 # substitui na lista []
num.append(7) # adiciona o 7
num.sort(reverse=True) # em ordem
num.insert(2,0) # na posiçao 2 adicione o 0
num.pop(2) # remove um elemento [2]
if 4 in num:
    num.remove(4) # remove o 4
else:
    print('Nao encontrei o 4')
print(num)
print(f'Essa lista tem {len(num)} elementos')