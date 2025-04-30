alturas = [ 1.80, 1.55, 1.74, 1.83, 1.60, 1.67, 1.79, 1.85 ]

i       = len(alturas)
soma    = float(0)

#for altura in alturas:
#    soma    += float(altura)

soma = sum(alturas)

divisao = soma / i

print(divisao)
