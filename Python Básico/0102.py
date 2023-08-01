
def fat(n, show=False):
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(c, end='')
            print(f' x ', end='')
        else:
            print(' = ', end='')
        f *= c
    return f

print(fat(5, show=True))