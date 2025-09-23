from pymongo import MongoClient

class Database:
    def __init__(self, uri="mongodb://localhost:27017", db_name="app_motoristas"):
        self.uri = uri
        self.db_name = db_name
        self.client = None
        self.db = None
        self.connect()

    def connect(self):
        try:
            self.client = MongoClient(self.uri)
            self.db = self.client[self.db_name]
            self.client.admin.command('ping')
            print(f"Conectado ao MongoDB em {self.uri}")
        except Exception as e:
            print("Erro ao conectar ao MongoDB:", e)
            raise

    def collection(self, name: str):
        return self.db[name]
