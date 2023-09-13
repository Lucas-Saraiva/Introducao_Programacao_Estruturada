vlrDepositoInicial = float(input("Valor deposito: "))
taxaJuros   = float(input("Taxa de juros: "))

vlrJuros = float(vlrDepositoInicial)

meses = int(0)

while meses <= 24:
    vlrDepositoMes = float(input(f"Valor do deposito no mês {meses}"))
    vlrJuros += vlrDepositoInicial
    vlrJuros += vlrJuros * ( taxaJuros / 100 )
    meses += 1

print(vlrJuros)
