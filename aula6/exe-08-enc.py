class cl_transporte():

    def __init__(self):
        self.transportes = [ 'Carro', 'Moto', 'Ônibus', 'Metro' ]

    def valida_lista(self, string):
        if string in self.transportes:
            return True
        else:
            return False

    def insere_item(self, transporte):
        self.transportes.append(transporte)

    def mostra_lista(self):
        print(self.transportes)
    

transportes = cl_transporte()

transportes.mostra_lista()

transporte = str(input("Digite o transporte que você mais utiliza: "))

resultado = transportes.valida_lista(transporte)

print(resultado)

if resultado == False:
    questao = str(input("Deseja inserir novo item: [S/N] "))

    if questao == 'S':
        transportes.insere_item(transporte)

transportes.mostra_lista()
