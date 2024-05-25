import os
from tinydb import TinyDB

basePath = os.getcwd() + "/db"

class DB:
    def __init__(self):
        self.db = TinyDB(basePath + "/index")
    
    def insert(self, tableName, data):
        table = self.db.table(tableName)

        table.insert(data)

    def get_all(self, tableName):
        table = self.db.table(tableName)

        return table.all()
