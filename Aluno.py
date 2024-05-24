# aluno.py
import pickle
from credito import Credito

class Aluno:
    def __init__(self, nome, cpf, matricula):
        self.nome = nome
        self.cpf = cpf
        self.matricula = matricula
        self.credito = Credito()
        self.auxilios = []

    def __str__(self):
        return f"Aluno: {self.nome}, CPF: {self.cpf}, Matrícula: {self.matricula}, Crédito: R${self.credito.saldo:.2f}"

    def adicionar_auxilio(self, auxilio):
        self.credito.adicionar_credito(auxilio.valor)
        self.auxilios.append(auxilio)
        print(f"Auxílio {auxilio.tipo} de R${auxilio.valor:.2f} adicionado ao aluno {self.nome}.")

    def exibir_auxilios(self):
        if not self.auxilios:
            print(f"{self.nome} não possui auxílios.")
        else:
            print(f"Auxílios de {self.nome}:")
            for auxilio in self.auxilios:
                print(f" - {auxilio}")

    def exibir_saldo(self):
        print(f"Saldo atual de {self.nome}: R${self.credito.saldo:.2f}")
        
    @staticmethod
    def salvar_alunos(alunos, filename="alunos.pkl"):
        with open(filename, 'wb') as file:
            pickle.dump(alunos, file)
        print("Alunos salvos com sucesso.")

    @staticmethod
    def carregar_alunos(filename="alunos.pkl"):
        try:
            with open(filename, 'rb') as file:
                alunos = pickle.load(file)
            print("Alunos carregados com sucesso.")
            return alunos
        except FileNotFoundError:
            print("Arquivo não encontrado. Iniciando com lista de alunos vazia.")
            return []
