cigarros = int(input("Quantidade de cigarros por dia: "))
anosFumante = int(input("Quantidade de anos fumando: "))

cigarrosFumados = ( anosFumante * 365 ) * cigarros
minutosPerdidos = cigarrosFumados * 10

diasPerdidos = minutosPerdidos / 1440

print(diasPerdidos)
