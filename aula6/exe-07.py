def valida_string(string: str, max: int, min: int):
    tamanho = len(string)
    if tamanho >= min and tamanho <= max:
        return True
    else:
        return False

texto = str(input("Digite um texto: "))
num_max = float(input("Digite o número máximo de caracteres: "))
num_min = float(input("Digite o número mínimo de caracteres: "))

resultado = valida_string(texto, num_max, num_min)

print(resultado)
print(valida_string(texto, num_max, num_min))
