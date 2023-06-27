test = list()
test.append('Gustavo')
test.append(40)
turm = list()
turm.append(test[:])
test[0] = 'Maria'
test[1] = 22
turm.append(test[:])
print(turm)