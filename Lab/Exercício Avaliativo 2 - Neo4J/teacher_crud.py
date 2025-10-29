from database import Database

class TeacherCRUD:
    def __init__(self, database: Database):
        self.db = database

    def create(self, name, ano_nasc, cpf):
        query = f"""
        CREATE (:Teacher {{name: '{name}', ano_nasc: {ano_nasc}, cpf: '{cpf}'}})
        """
        self.db.execute_query(query)
        print(f"Professor {name} criado com sucesso!")

    def read(self, name):
        query = f"""
        MATCH (t:Teacher {{name: '{name}'}})
        RETURN t.name, t.ano_nasc, t.cpf
        """
        result = self.db.execute_query(query)
        if result:
            print("Professor encontrado:", result[0])
        else:
            print("Professor não encontrado.")
        return result

    def update(self, name, newCpf):
        query = f"""
        MATCH (t:Teacher {{name: '{name}'}})
        SET t.cpf = '{newCpf}'
        RETURN t
        """
        self.db.execute_query(query)
        print(f"CPF do professor {name} atualizado para {newCpf}!")

    def delete(self, name):
        query = f"""
        MATCH (t:Teacher {{name: '{name}'}})
        DELETE t
        """
        self.db.execute_query(query)
        print(f"Professor {name} deletado com sucesso!")
