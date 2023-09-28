from time import sleep

def valida_lista(string, lista):
    if string in lista:
        return True
    else:
        return False

print("Carro \n"
      "Moto \n"
      "Ônibus \n"
      "Metro")

sleep(1.5)

transporte = str(input("Digite o transporte que você mais utiliza: "))

lista = [ 'Carro', 'Moto', 'Ônibus', 'Metro' ]

resultado = valida_lista(transporte, lista)

print(resultado)
