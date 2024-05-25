import os
from tinydb import TinyDB

basePath = os.getcwd() + "/db"

class DB:
    def __init__(self, name):
        self.name = name
        self.db = TinyDB(basePath + "/" + name)
    
    def insert(self, data):
        self.db.insert(data)
