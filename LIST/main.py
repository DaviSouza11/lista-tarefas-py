from funcoes import adicionar_atividade, mostrar_atividade, remover_atividade, carregar_tarefas, salvar_tarefas

carregar_tarefas()

print(f"Bem vindo a sua Lista de Tarefas: ")

while True:
    texto_menu = """
    --- MENU PRINCIPAL ---
    1 - Adicionar item a lista:
    2 - Remover item da lista:
    3 - Ver itens da lista:
    4 - Sair.
    ----------------------------
    Escolha uma opção: 
    """

    escolha = input(texto_menu)

    match escolha:
        case "1":
            adicionar_atividade()
            salvar_tarefas()
        case "2":
            remover_atividade()
            salvar_tarefas()
        case "3":
            mostrar_atividade()
        case "4":
            print("Saindo do progama.")
            break
        case _:
            print("Opção inválida. Tente Novamente.")


