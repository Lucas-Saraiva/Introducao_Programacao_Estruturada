def area_triangulo(base: float, altura: float):
    return((base * altura)/2)

base    = float(input("Digite a base do triângulo: "))
altura  = float(input("Digite a altura do triângulo: "))

resultado = area_triangulo(base, altura)

print(resultado)
print(area_triangulo(base, altura))
