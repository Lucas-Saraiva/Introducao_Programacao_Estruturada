kmViagem = float(input("Quantidade de Km da viagem: "))

if kmViagem <= 200.00:
    vlrViagem = 0.45 * kmViagem
else:
    vlrViagem = 0.45 * kmViagem

print(f"O valor da sua viagem será de R$ {vlrViagem:.2f}")
