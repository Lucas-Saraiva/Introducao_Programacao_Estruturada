qtdQuestao = int(1)

nota = int(0)

while qtdQuestao <= 3:
    resposta = str(input("Alteranativa: "))
    match qtdQuestao:
        case 1:
            if resposta == "B" or resposta == "b":
                nota += 1
        case 2:
            if resposta == "A" or resposta == "a":
                nota += 1
        case 3:
            if resposta == "D" or resposta == "d":
                nota += 1
    
    qtdQuestao += 1

print(nota)
