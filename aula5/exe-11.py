vlrDeposito = float(input("Valor deposito: "))
taxaJuros   = float(input("Taxa de juros: "))

vlrJuros = float(vlrDeposito)

meses = int(24)

while meses > 0:
    vlrJuros += vlrJuros * ( taxaJuros / 100 )
    meses -= 1

print(vlrJuros)
