primeiraVenda = [ "maça", "pera", "banana" ]
segundaVenda = [ "abacaxi", "pera", "limão", "limão" ]

for itemVenda in segundaVenda:
    if itemVenda in primeiraVenda:
        primeiraVenda.remove(itemVenda)
    else:
        primeiraVenda.append(itemVenda)

print(primeiraVenda)
