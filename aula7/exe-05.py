from time import sleep

senhas = [0]

x = True

senha = int(0)

while x:
    print("Para gera uma senha digite: 1 \n"
          "Para voltar ao menu: 2: \n"
          "Para finalizar o atendimento: S")
    sleep(2)
    questao = str(input("Operação desejada: "))

    match questao:
        case '1':
            senha += 1
            senhas.append(senha)
            print(f"Sua senha para atendimento é: {senha}")
        case '2':
            pass
        case 'S':
            x = False
        case _:
            print("Opção inválida!")

    sleep(2)
