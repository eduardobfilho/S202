from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["Biblioteca"]

db.drop_collection("Livros")
db.create_collection("Livros", validator={
    "$jsonSchema": {
        "bsonType": "object",
        "required": ["_id", "titulo", "autor", "ano", "preco"],
        "properties": {
            "_id": {"bsonType": "int"},
            "titulo": {"bsonType": "string"},
            "autor": {"bsonType": "string"},
            "ano": {"bsonType": "int"},
            "preco": {"bsonType": ["double", "int"]}
        }
    }
})

try:
    db.Livros.insert_many([
        {"_id": 1, "titulo": "Clean Code", "autor": "Robert C. Martin", "ano": 2008, "preco": 31.0},
        {"_id": 2, "titulo": "Harry Potter and the Philosopher's Stone", "autor": "J.K. Rowling", "ano": 1997, "preco": 31.0}
    ])
except:
    pass

def menu():
    while True:
        print("\n=== Biblioteca - Menu ===")
        print("1. Inserir livro")
        print("2. Listar livros")
        print("3. Buscar livro por ID")
        print("4. Atualizar livro")
        print("5. Remover livro")
        print("0. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            inserir_livro()
        elif opcao == "2":
            listar_livros()
        elif opcao == "3":
            buscar_livro()
        elif opcao == "4":
            atualizar_livro()
        elif opcao == "5":
            remover_livro()
        elif opcao == "0":
            print("Saindo...")
            break
        else:
            print("Opção inválida!")

def inserir_livro():
    try:
        _id = int(input("ID: "))
        titulo = input("Título: ")
        autor = input("Autor: ")
        ano = int(input("Ano: "))
        preco = float(input("Preço: "))

        livro = {"_id": _id, "titulo": titulo, "autor": autor, "ano": ano, "preco": preco}
        db.Livros.insert_one(livro)
        print("Livro inserido com sucesso!")
    except Exception as e:
        print("Erro ao inserir:", e)

def listar_livros():
    for livro in db.Livros.find():
        print(livro)

def buscar_livro():
    try:
        _id = int(input("Digite o ID do livro: "))
        livro = db.Livros.find_one({"_id": _id})
        if livro:
            print(livro)
        else:
            print("Livro não encontrado.")
    except Exception as e:
        print("Erro:", e)

def atualizar_livro():
    try:
        _id = int(input("Digite o ID do livro a atualizar: "))
        campo = input("Qual campo deseja atualizar (titulo, autor, ano, preco): ")
        valor = input("Novo valor: ")

        if campo in ["ano", "preco"]:
            valor = float(valor) if campo == "preco" else int(valor)

        resultado = db.Livros.update_one({"_id": _id}, {"$set": {campo: valor}})
        if resultado.modified_count > 0:
            print("Livro atualizado com sucesso!")
        else:
            print("Nenhum livro foi atualizado.")
    except Exception as e:
        print("Erro:", e)

def remover_livro():
    try:
        _id = int(input("Digite o ID do livro a remover: "))
        resultado = db.Livros.delete_one({"_id": _id})
        if resultado.deleted_count > 0:
            print("Livro removido com sucesso!")
        else:
            print("Nenhum livro encontrado para remover.")
    except Exception as e:
        print("Erro:", e)

# Executar menu
if __name__ == "__main__":
    menu()
