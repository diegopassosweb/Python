
num = [2,5,4,1]
num[2] = 3
num.append(7)
num.sort(reverse=True)
num.insert(2, 0)
num.remove(2)
if 4 in num:
    num.remove(4)
else:
    print('Nao achei')
#num.pop(2)
print(num)
print(f'Essa lista tem {len(num)} elementos')