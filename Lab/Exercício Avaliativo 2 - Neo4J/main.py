from database import Database
from teacher_crud import TeacherCRUD

def main():
    db = Database("bolt://localhost:7687", "neo4j", "neo4jtest")
    teacher_crud = TeacherCRUD(db)

    while True:
        print("\n=== MENU TEACHER CRUD ===")
        print("1 - Criar Teacher")
        print("2 - Ler Teacher")
        print("3 - Atualizar CPF")
        print("4 - Deletar Teacher")
        print("5 - Criar Chris Lima (Teste da prova)")
        print("6 - Sair")

        op = input("Escolha uma opção: ")

        if op == '1':
            name = input("Nome: ")
            ano = int(input("Ano de nascimento: "))
            cpf = input("CPF: ")
            teacher_crud.create(name, ano, cpf)
        elif op == '2':
            name = input("Nome do professor: ")
            teacher_crud.read(name)
        elif op == '3':
            name = input("Nome do professor: ")
            newCpf = input("Novo CPF: ")
            teacher_crud.update(name, newCpf)
        elif op == '4':
            name = input("Nome do professor: ")
            teacher_crud.delete(name)
        elif op == '5':
            teacher_crud.create("Chris Lima", 1956, "189.052.396-66")
            teacher_crud.read("Chris Lima")
            teacher_crud.update("Chris Lima", "162.052.777-77")
        elif op == '6':
            print("Encerrando o sistema...")
            break
        else:
            print("Opção inválida!")

    db.close()

if __name__ == "__main__":
    main()
