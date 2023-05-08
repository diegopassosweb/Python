def contador(*num):
    tam = len(num)
    print(f' Recebi os valores {num} e sao ao todo {tam} numeros', end="")

contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)