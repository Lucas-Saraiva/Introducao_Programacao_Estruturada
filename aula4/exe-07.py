vlrProduto = float(input("Valor produto"))

if vlrProduto < 10.00:
    print("O produto é de categoria 1")
elif vlrProduto > 10.00 and vlrProduto < 15.00:
    print("O produto é de categoria 2")
elif vlrProduto > 15.00 and vlrProduto < 19.00:
    print("O produto é de categoria 3")
elif vlrProduto > 19.00 and vlrProduto < 23.00:
    print("O produto é de categoria 4")
elif vlrProduto > 23.00 and vlrProduto < 27.00:
    print("O produto é de categoria 5")
