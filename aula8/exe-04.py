nomes = {}

palavra = str(input("Digite uma palavra: "))

cont = int(0)

for caracter in palavra:
    nomes[caracter] = cont
    cont += 1

print(nomes)

# nomes = [ ]

# palavra = str(input("Digite uma palavra: "))

# cont = int(0)

# for caracter in palavra:
#     nome = {"letra": caracter, "posicao": cont}
#     cont += 1
#     nomes.append(nome)

# print(nomes)
