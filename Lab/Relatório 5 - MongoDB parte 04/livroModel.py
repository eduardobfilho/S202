class LivroModel:
    def __init__(self, database):
        self.collection = database["Livros"]

    def create_livro(self, _id: int, titulo: str, autor: str, ano: int, preco: float):
        try:
            res = self.collection.insert_one({
                "_id": _id,
                "titulo": titulo,
                "autor": autor,
                "ano": ano,
                "preco": preco
            })
            print(f"✅ Livro criado com id: {res.inserted_id}")
        except Exception as e:
            print(f"❌ Erro ao criar livro: {e}")

    def read_livro_by_id(self, _id: int):
        livro = self.collection.find_one({"_id": _id})
        if livro:
            print(f"📖 {livro}")
        else:
            print("⚠️ Livro não encontrado")

    def update_livro(self, _id: int, campo: str, valor):
        res = self.collection.update_one({"_id": _id}, {"$set": {campo: valor}})
        print("✅ Atualizado!" if res.modified_count > 0 else "⚠️ Nenhum livro alterado.")

    def delete_livro(self, _id: int):
        res = self.collection.delete_one({"_id": _id})
        print("✅ Removido!" if res.deleted_count > 0 else "⚠️ Nenhum livro encontrado.")

    def list_all(self):
        for livro in self.collection.find():
            print(livro)
