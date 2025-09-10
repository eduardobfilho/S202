from pymongo import MongoClient
import json

def get_database():
    client = MongoClient("mongodb://localhost:27017/")
    db = client["Biblioteca"]

    with open("validation.txt", "r", encoding="utf-8") as f:
        validation = json.load(f)

    db.drop_collection("Livros")
    db.create_collection("Livros", validator=validation)

    return db
