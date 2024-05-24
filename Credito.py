# credito.py
class Credito:
    def __init__(self):
        self.saldo = 0.0

    def adicionar_credito(self, valor):
        self.saldo += valor
        print(f"Crédito de R${valor:.2f} adicionado. Saldo atual: R${self.saldo:.2f}")

    def debitar_credito(self, valor):
        if valor > self.saldo:
            print("Saldo insuficiente.")
            return False
        self.saldo -= valor
        print(f"R${valor:.2f} debitado. Saldo atual: R${self.saldo:.2f}")
        return True