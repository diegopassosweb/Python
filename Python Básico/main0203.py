

def dobra(ist):
    pos = 0
    while pos < len(ist):
        ist[pos]*= 2
        pos += 1
        
valores = [6, 3, 9, 1, 0, 2]
dobra(valores)
print(valores)