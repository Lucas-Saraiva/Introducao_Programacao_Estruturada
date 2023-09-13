numero1 = float(input("Primeiro número: "))
numero2 = float(input("Segundo número: "))
numero3 = float(input("Terceiro número: "))

if numero1 > numero2 and numero1 > numero3:
    print("Primeiro número é o maior")
elif numero2 > numero1 and numero1 > numero3:
    print("Segundo número é o maior")
elif numero3 > numero1 and numero3 > numero2:
    print("Terceiro número é o maior")

if numero1 < numero2 and numero1 < numero3:
    print("Primeiro número é o menor")
elif numero2 < numero1 and numero1 < numero3:
    print("Segundo número é o menor")
elif numero3 < numero1 and numero3 < numero2:
    print("Terceiro número é o menor")
