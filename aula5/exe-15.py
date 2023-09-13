codigoProduto   = int(input("Código do produto: "))
qtdCompra       = int(input("Quantidade comprada: "))

match codigoProduto:
    case _:
        print("Código Inválido!")
    case 1:
        print(qtdCompra * 0.50)
    case 2:
        print(qtdCompra * 1)
    case 4:
        print(qtdCompra * 4)
    case 5:
        print(qtdCompra * 7)
    case 9:
        print(qtdCompra * 8)
