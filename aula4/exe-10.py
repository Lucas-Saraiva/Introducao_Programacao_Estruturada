qtdKWr = float(input("Quantidade de kWr: "))

print("Tipos de Instalação \n"
        "R Residencial \n"
        "I Industrial \n"
        "C Comércio")

tipoInstalacao = str(input("Tipo de instalação: "))

match tipoInstalacao:
    case "R":
        if qtdKWr > 500:
            vlrKWr = qtdKWr * 0.65
        else:
            vlrKWr = qtdKWr * 0.40

    case "C":
        if qtdKWr > 1000:
            vlrKWr = qtdKWr * 0.55
        else:
            vlrKWr = qtdKWr * 0.60

    case "I":
        if qtdKWr > 5000:
            vlrKWr = qtdKWr * 0.55
        else:
            vlrKWr = qtdKWr * 0.60

print(vlrKWr)
