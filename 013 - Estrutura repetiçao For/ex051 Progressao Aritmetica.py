p = int(input('Primeiro termo: '))
r = int(input('Razao: '))
d = p + (10 - 1) * r
for c in range (p, d + r, r):
    print(f' {c}', end=" → ")
print('fim')