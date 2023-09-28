def div(num1: int, num2: int):
    if ( num1 % num2 ) == 0:
        return True
    else:
        return False

num1 = int(input("Digite o primeiro número: ")) 
num2 = int(input("Digite o segundo número: "))

resultado = div(num1, num2)

print(resultado)
print(div(num1, num2))
