num = int(input("Núemro desejado: "))
cont = 1

while cont <= num:
    cont += 1
    resto = cont % 2
    if resto != 0:
        print(cont)
