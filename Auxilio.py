# auxilio.py
class Auxilio:
    def __init__(self, tipo, valor):
        self.tipo = tipo
        self.valor = valor

    def __str__(self):
        return f"Auxílio: {self.tipo}, Valor: R${self.valor:.2f}"