a = input("Digite algo: ")
print(f"O tipo primitivo do valor é {type(a)}")
print(f"Só tem espaços? {a.isspace()}")
print(f"É um numero? {a.isnumeric()}")
print(f"É alfabetico? {a.isalpha()}")
print(f"É alfanumerico? {a.isalnum()}")
print(f"Está em MAIUSCULAS? {a.isupper()}")
print(f"Está em minusculas? {a.islower()}")
print(f"Está Capitalizada? {a.istitle()}")