def maximo(a: int, b: int):
    if a > b:
        return(a)
    else:
        return(b)

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

vl_num = maximo(num1, num2)

print(vl_num)
print(maximo(num1, num2))
