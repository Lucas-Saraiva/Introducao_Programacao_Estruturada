mult1 = int(input("Multiplicado: "))
mult2 = int(input("Multiplicador: "))

cont        = int(1)
resultado   = int(0)

while cont <= mult2:
    resultado += mult1
    cont += 1

print(resultado)

resultado = 0

for i in range(0, mult2):
    resultado += mult1  

print(resultado)