from Passageiro import Passageiro
from Corrida import Corrida
from Motorista import Motorista
import pprint

class MotoristaCLI:
    def __init__(self, dao):
        self.dao = dao
        self.commands = {
            "create": self.create,
            "list": self.list_all,
            "read": self.read_by_id,
            "update": self.update,
            "delete": self.delete,
            "add_corrida": self.add_corrida,
            "calc_nota": self.calc_nota_media,
            "help": self.help,
            "quit": self.quit,
        }
        self.running = True

    def run(self):
        print("Bem-vindo ao Motorista CLI!")
        print("Comandos: create, list, read, update, delete, add_corrida, calc_nota, help, quit")
        while self.running:
            cmd = input("Comando: ").strip()
            func = self.commands.get(cmd)
            if func:
                try:
                    func()
                except Exception as e:
                    print("Erro:", e)
            else:
                print("Comando inválido.")

    def help(self):
        print("create, list, read, update, delete, add_corrida, calc_nota, quit")

    def quit(self):
        self.running = False
        print("Saindo...")

    def create(self):
        nome_p = input("Nome do passageiro: ")
        doc_p = input("Documento do passageiro: ")
        passageiro = Passageiro(nome_p, doc_p)

        corridas = []
        while True:
            nota = int(input("Nota (0-5): "))
            distancia = float(input("Distância: "))
            valor = float(input("Valor: "))
            corridas.append(Corrida(nota, distancia, valor, passageiro))
            if input("Adicionar outra corrida? (s/n): ").lower() != "s":
                break

        nome_m = input("Nome do motorista: ")
        doc_m = input("Documento do motorista: ")
        motorista = Motorista(nome_m, doc_m, corridas)
        _id = self.dao.create_motorista(motorista)
        print("Motorista criado com id:", _id)

    def list_all(self):
        docs = self.dao.list_motoristas()
        for d in docs:
            pprint.pprint(d)
            print("-" * 30)

    def read_by_id(self):
        _id = input("ID do motorista: ")
        d = self.dao.get_motorista(_id)
        pprint.pprint(d) if d else print("Não encontrado.")

    def update(self):
        _id = input("ID do motorista: ")
        nome = input("Novo nome (ou Enter): ")
        doc = input("Novo documento (ou Enter): ")
        updates = {}
        if nome: updates["nome"] = nome
        if doc: updates["documento"] = doc
        print("Atualizado." if self.dao.update_motorista(_id, updates) else "Falhou.")

    def delete(self):
        _id = input("ID do motorista: ")
        print("Deletado." if self.dao.delete_motorista(_id) else "Falhou.")

    def add_corrida(self):
        _id = input("ID do motorista: ")
        nota = int(input("Nota: "))
        distancia = float(input("Distância: "))
        valor = float(input("Valor: "))
        nome_p = input("Nome passageiro: ")
        doc_p = input("Documento passageiro: ")
        corrida = Corrida(nota, distancia, valor, Passageiro(nome_p, doc_p))
        print("OK" if self.dao.add_corrida(_id, corrida) else "Falhou.")

    def calc_nota_media(self):
        _id = input("ID do motorista: ")
        media = self.dao.calcular_nota_media(_id)
        print("Média:", media if media else "Sem corridas.")
