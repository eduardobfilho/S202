from database import get_database
from livroModel import LivroModel
from cli import menu

if __name__ == "__main__":
    db = get_database()
    livros = LivroModel(db)

    # Inserindo exemplos iniciais
    try:
        livros.create_livro(1, "Clean Code", "Robert C. Martin", 2008, 31.0)
        livros.create_livro(2, "Harry Potter and the Philosopher's Stone", "J.K. Rowling", 1997, 31.0)
    except:
        pass

    # Chama o menu
    menu(livros)
