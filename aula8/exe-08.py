primeiraVenda = [ "maça", "pera", "banana" ]
segundaVenda = [ "abacaxi", "pera", "limão", "limão" ]

novaLista = []

for itemVenda in primeiraVenda:
    if itemVenda in novaLista:
        novaLista.remove(itemVenda)
    else:
        novaLista.append(itemVenda)

for itemVenda in segundaVenda:
    if itemVenda in novaLista:
        novaLista.remove(itemVenda)
    else:
        novaLista.append(itemVenda)

print(novaLista)
