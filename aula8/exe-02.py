estoque = { "maça": { "quantidade": 3, "valor": 10.0 },
            "pera": { "quantidade": 5, "valor": 11.5},
            "uva": { "quantidade": 10, "valor": 15.0 },
            "carambola": { "quantidade": 8, "valor": 7.50 },
            "banana": { "quantidade": 12, "valor": 6.50 } }

vendas = [  { "fruta": "maça", "quantidade": 1 },
            { "fruta": "pera", "quantidade": 1} ]

total = float(0)

for venda in vendas:
    material = venda.get("fruta")
    quantidade = venda.get("quantidade")

    valor = estoque[material]["valor"]
    total += valor

    estoque[material]["quantidade"] -= quantidade 
    print(estoque[material])

print(total)
