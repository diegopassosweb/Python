renda_mensal = float(input('Digite sua renda mensal R$ '))

obter50 = (50 / 100) * renda_mensal
obter30 = (30 / 100) * renda_mensal
obter20 = (20 / 100) * renda_mensal

print("=======\nSeus numeros de 50% 30% 20% \n========")

print("Necessidades: R${:,.2f}".format(obter50))
print("Gastos: R${:,.2f}".format(obter30))
print("Poupança: R${:,.2f}".format(obter20))

print("\n================================================\n")