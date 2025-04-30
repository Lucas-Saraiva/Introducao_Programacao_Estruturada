primeiraVenda = [ "maça", "pera", "banana" ]
segundaVenda = [ "abacaxi", "pera", "limão" ]

novaLista = []

for itemPrimeiraVenda in primeiraVenda:
    if itemPrimeiraVenda not in segundaVenda:
        novaLista.append(itemPrimeiraVenda)

print(novaLista)
