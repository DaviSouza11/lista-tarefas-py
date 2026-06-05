tarefas = []

def adicionar_atividade():
    nova_tarefa = input("O que você precisa fazer?\n")
    tarefas.append(nova_tarefa)
    print(f"Nova Tarefa: {nova_tarefa},adicionada com sucesso!\n")


def mostrar_atividade():
    if len(tarefas) == 0:
        print("A sua lista esta vazia!")
    else:
        for t in tarefas:
            print(f"-{t}")

def remover_atividade():
    remover_tarefa = input(f"Qual tarefa você deseja remover da sua lista?\n{tarefas}\n")

    if remover_tarefa in tarefas:
        tarefas.remove(remover_tarefa)
        print(f"\nA tarefa '{remover_tarefa}' foi removida com sucesso!")
    else:
        print("Erro: A tarefa não foi encontrada em sua lista!")

def salvar_tarefas():
    # O "w" é write. Ele cria o arquivo e substitui o antigo - encoding="utf-8" garante que carácteres especiais sejam considerados e salvos corretamente
    with open("minhas_tarefas.txt", "w", encoding="utf-8") as arquivo:
              for t in tarefas:
                arquivo.write(t + "\n")

def carregar_tarefas():
    try:    
        # O "r" é read.
        with open("minhas_tarefas.txt", "r", encoding="utf-8") as arquivo:
            for linha in arquivo:
                # O .strip() limpa espaços vazios e os \n
                tarefas.append(linha.strip())
    except FileNotFoundError:
        pass        