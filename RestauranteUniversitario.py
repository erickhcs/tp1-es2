# RestauranteUniversitario.py
class RestauranteUniversitario:
    def __init__(self, preco_refeicao=4.0):
        self.preco_refeicao = preco_refeicao

    def pagar_refeicao(self, usuario):
        if usuario.credito.debitar_credito(self.preco_refeicao):
            print("Refeição paga com sucesso.")
        else:
            print("Pagamento da refeição falhou.")