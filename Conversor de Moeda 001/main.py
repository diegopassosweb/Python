def main():
    print("Este programa converte dolar para Pounds")
    print()
    
    dolar = eval(input("Digite a quantidade de dolares: "))
    
    pounds = convert_to_pounds(dolar)
    
    print("Foi convertido", pounds, "pounds")

convert_to_pounds = lambda dolar: dolar * 0.82

main()