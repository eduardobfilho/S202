from Database import Database
from MotoristaDAO import MotoristaDAO
from MotoristaCLI import MotoristaCLI

def main():
    db = Database()
    dao = MotoristaDAO(db)
    cli = MotoristaCLI(dao)
    cli.run()

if __name__ == "__main__":
    main()
