estoque = { "maça": { "quantidade": 3, "valor": 10.0 },
            "pera": { "quantidade": 5, "valor": 11.5},
            "uva": { "quantidade": 10, "valor": 15.0 },
            "carambola": { "quantidade": 8, "valor": 7.50 },
            "banana": { "quantidade": 12, "valor": 6.50 } }

venda = { "fruta": str, "quantidade": int }

total = float(0)

x = True

while x:

    questao = str(input("Deseja registrar uma venda? [S/N] "))
    if questao == 'S':
        venda["fruta"] = str(input("Fruta comprada: "))
        venda["quantidade"] = int(input("Quantidade: "))

        material = venda.get("fruta")
        quantidade = venda.get("quantidade")

        valor = estoque[material]["valor"]
        total += valor

        estoque[material]["quantidade"] -= quantidade 
        print(estoque[material])
    else:
        x = False

print(total)
