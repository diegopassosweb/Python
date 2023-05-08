def dobra(num):
    pos = 0
    while pos < len(num):
        num[pos] *= 2
        pos += 1
        
valores = [4,5,6,7,8,9]
dobra(valores)
print(valores)