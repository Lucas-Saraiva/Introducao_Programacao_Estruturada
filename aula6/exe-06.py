def mdc(a: int, b: int):
    if b == 0:
        return a
    else:
        return mdc(b, ( a % b ) )

def mmc(a, b):
    return abs(a * b) / mdc(a, b)

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

resultado = mmc(num1, num2)

print(resultado)
print(mmc(num1, num2))
