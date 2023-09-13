numero1 = float(input("Primeiro número: "))
numero2 = float(input("Segundo número: "))

print("Operações permitidas \n"
        "+ Soma \n"
        "- Subtração \n "
        "* Multiplicação \n"
        "/ Divisão")

operacao = str(input("Operação matemática desejada: "))

match operacao:
    case '+':
        resultado = numero1 + numero2
    case '-':
        resultado = numero1 - numero2
    case '*':
        resultado = numero1 * numero2
    case '/':
        resultado = numero1 / numero2

print(resultado)
