x = False

qtd = int(0)
total = int(0)

while x == False:
    num = int(input("Número: "))
    if num == 0:
        x = True
    else:
        qtd += 1
        total += num

media = total / qtd

print(f"Quantidade digitada é {qtd}")
print(f"Valor total digitado é {total}")
print(f"Média dos valores digitados é {media}")
