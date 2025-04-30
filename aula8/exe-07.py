primeiraVenda = [ "maça", "pera", "banana" ]
segundaVenda = [ "abacaxi", "pera", "limão" ]

novaLista = []

for itemSegundaVenda in segundaVenda:
    if itemSegundaVenda not in primeiraVenda:
        novaLista.append(itemSegundaVenda)

print(novaLista)
