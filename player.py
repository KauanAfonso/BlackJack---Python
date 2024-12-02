class Player:
    def __init__(self, name):
        self.name = name
        self.name = input("Entre com seu nome: ")  # Permite alterar o nome

    def get_name(self):
        return self.name

