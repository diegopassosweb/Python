med = float(input("Uma distancia em metros: "))
cm = med * 100
mm = med * 1000
dm = med * 10
dam = med / 10
hm = med / 100
km = med / 1000
print(f'A medida de {med} metros é {cm:.0f} centimentos e ')
print(f'A medida de {med} é {mm:.0f} milimetros')
print(f'A medida de {med} é {dm} decimetros')
print(f'A medida de {med} é {dam} decametros')
print(f'A medida de {med} é {hm} hectrometro')
print(f'A medida de {med} é {km} quilometro')

# :.0f (nenhuma casa decimal)
# :.1f(somente uma casa decimal)
# :.2f(somente duas casas decimais)
# :.3f(somente três casas decimais)