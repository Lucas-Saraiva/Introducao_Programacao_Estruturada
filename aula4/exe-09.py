vlrCasa = float(input("Valor da casa: "))
vlrSalario = float(input("Seu Salário: "))
qtdAnos = int(input("Quantidade de anos: "))

qtdMeses = qtdAnos * 12
vlrMensalCasa = vlrCasa / qtdMeses

vlrSalarioPercentual = vlrSalario * ( 30 / 100 )

if vlrSalarioPercentual > vlrMensalCasa:
    print(f"Valor da prestação é maior que o permitido! Valor é de {vlrMensalCasa}")
else:
    print(f"Valor dentro da permissão da prestação! Valor é de {vlrMensalCasa}")
