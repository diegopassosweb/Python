

def notas(*n, sit=False):
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['media'] = sum(n)/len(n)
    if sit:
        if r['media'] > 7:
            r['situation'] = 'BOA'
        elif r['situation'] >= 5:
            r['situation'] = 'RAZOAVEL'
        else:
            r['situation'] = 'RUIM'
    return r
r = notas(5.4, 3.5,9.5,4,8)
print(r)