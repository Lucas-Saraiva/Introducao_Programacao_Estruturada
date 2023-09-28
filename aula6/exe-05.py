def mdc(a: int, b: int):
    if b == 0:
        return a
    else:
        return mdc(b, (a % b) )

a = int(input("Digite um número: "))
b = int(input("Digite outro número: "))

resultado = mdc(a, b)
print(resultado)
print(mdc(a, b))
