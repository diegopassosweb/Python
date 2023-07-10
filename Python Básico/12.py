preco = float(input('Digite o preço do produto: R$'))
novo = preco - (preco * 5 / 100)
print(f'O produto de R${preco:.2f} com 5% de desconto custa R${novo:.2f}')
