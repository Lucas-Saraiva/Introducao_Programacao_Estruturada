valor = float(input("Digite um valor: "))

cedulas = 0

while valor >= 1:

    if valor >= 100:
        valor   -= 100
        cedulas += 1
        if valor < 100:
            print(f"Foram utilizadas {cedulas} cédulas de 100 reais")
            cedulas = 0        

    elif valor >= 50:
        valor   -= 50
        cedulas += 1
        if valor < 50:
            print(f"Foram utilizadas {cedulas} cédulas de 50 reais")
            cedulas = 0

    elif valor >= 20:
        valor -= 20
        cedulas += 1
        if valor < 20:
            print(f"Foram utilizadas {cedulas} cédulas de 20 reais")
            cedulas = 0

    elif valor >= 10:
        valor -= 10
        cedulas += 1
        if valor < 10:
            print(f"Foram utilizadas {cedulas} cédulas de 10 reais")
            cedulas = 0

    elif valor >= 4:
        valor -= 4
        cedulas += 1
        if valor < 4:
            print(f"Foram utilizadas {cedulas} cédulas de 4 reais")
            cedulas = 0

    elif valor >= 1:
        valor -= 1
        cedulas += 1
        if valor < 1:
            print(f"Foram utilizadas {cedulas} cédulas de 1 real")
            cedulas = 0
