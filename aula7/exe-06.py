from time import sleep

senhasA = [0]
senhasB = [0]

x = True

senha = int(0)

while x:

    fila = str(input("Filas para atendimento: [ A/B ]"))

    print("Para gera uma senha digite: 1 \n"
          "Para voltar ao menu: 2: \n"
          "Para finalizar o atendimento: S")

    sleep(2)
    questao = str(input("Operação desejada: "))

    match questao:
        case '1':
            if fila == 'A':
                senha = 1 + senhasA.pop()
                senhasA.append(senha)
            elif fila == 'B':
                senha = 1 + senhasB.pop()
                senhasB.append(senha)
            
            print(f"Sua senha para atendimento é: {senha}")
        case '2':
            pass
        case 'S':
            x = False
        case _:
            print("Opção inválida!")

    sleep(2)
