n = []
me = 0
ma = 0
for c in range(0, 5):
    n.append(int(input(f"Digite um valor para a posiçao {c}: ")))
    if c == 0:
        ma = me = n[c]
    else:
        if n[c] > ma:
            ma = n[c]
        if n[c] < me:
            me = n[c]
print("-="*30)
print(f'Voce digitou {n} valores')
print(f'O maior valor foi {ma}')
for i, v in enumerate(n):
    if v == ma:
        print(f' {i}... ', end="")
print()
print(f'O menor valor foi {me}')
for i, v in enumerate(n):
    if v == me:
        print(f' {i}... ', end="")
print()