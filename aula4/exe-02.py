velocidade = int(input("Velocidade do carro: "))
vlrKmMulta = 5
velocidadeMaxima = 80

if velocidade > velocidadeMaxima:
    vlrMulta = ( velocidade - velocidadeMaxima ) * vlrKmMulta

    print(vlrMulta)
