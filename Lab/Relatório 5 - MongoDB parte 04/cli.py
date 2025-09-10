def menu(livros):
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
            _id = int(input("ID: "))
            titulo = input("Título: ")
            autor = input("Autor: ")
            ano = int(input("Ano: "))
            preco = float(input("Preço: "))
            livros.create_livro(_id, titulo, autor, ano, preco)

        elif opcao == "2":
            livros.list_all()

        elif opcao == "3":
            _id = int(input("ID: "))
            livros.read_livro_by_id(_id)

        elif opcao == "4":
            _id = int(input("ID: "))
            campo = input("Campo (titulo, autor, ano, preco): ")
            valor = input("Novo valor: ")
            if campo in ["ano", "preco"]:
                valor = float(valor) if campo == "preco" else int(valor)
            livros.update_livro(_id, campo, valor)

        elif opcao == "5":
            _id = int(input("ID: "))
            livros.delete_livro(_id)

        elif opcao == "0":
            print("👋 Saindo...")
            break
        else:
            print("❌ Opção inválida")
