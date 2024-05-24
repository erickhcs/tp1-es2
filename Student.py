# student.py
import pickle
from credit import Credit

class Student:
    def __init__(self, name, cpf, registration):
        self.name = name
        self.cpf = cpf
        self.registration = registration
        self.credit = Credit()
        self.aids = []

    def __str__(self):
        return f"Student: {self.name}, CPF: {self.cpf}, Registration: {self.registration}, Credit: ${self.credit.balance:.2f}"

    def add_aid(self, aid):
        self.credit.add_credit(aid.amount)
        self.aids.append(aid)
        print(f"Aid {aid.type} of ${aid.amount:.2f} added to student {self.name}.")

    def show_aids(self):
        if not self.aids:
            print(f"{self.name} has no aids.")
        else:
            print(f"Aids of {self.name}:")
            for aid in self.aids:
                print(f" - {aid}")

    def show_balance(self):
        print(f"Current balance of {self.name}: ${self.credit.balance:.2f}")

    @staticmethod
    def save_students(students, filename="students.pkl"):
        with open(filename, 'wb') as file:
            pickle.dump(students, file)
        print("Students saved successfully.")

    @staticmethod
    def load_students(filename="students.pkl"):
        try:
            with open(filename, 'rb') as file:
                students = pickle.load(file)
            print("Students loaded successfully.")
            return students
        except FileNotFoundError:
            print("File not found. Starting with an empty list of students.")
            return []
