preco = float(input("Valor do produto: "))
desconto = float(input("Percentual de desconto: "))

valorDesconto = preco * (desconto / 100)
valorPagar = preco - valorDesconto

print(f"Valor a pagar: {valorPagar}. Desconto: {valorDesconto}")
