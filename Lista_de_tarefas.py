import json

try:
    with open('tarefas.json', 'r') as f:
        tarefas = json.load(f)
except FileNotFoundError:
    tarefas = []

with open('tarefas.json', 'w') as f:
    json.dump(tarefas, f)


tarefas = []

while True:
    print("O que deseja fazer")
    print("1. Adicionar tarefa")
    print("2. Visualizar tarefa")
    print("3. Marcar como concluída")
    print("4. Remover tarefa")
    print("5. Sair")

    opcao = int(input("Digite a opção:"))

    if opcao == 1:
        tarefa = input("Digite a nova tarefa: ")
        tarefas.append(tarefa)
        print("Tarefa adicionada!")
    elif opcao == 2:
        print("Tarefas: ")
        for i, tarefa in enumerate(tarefas):
            print(f"{i+1}. {tarefa}")
    elif opcao == 3:
        indice = int(input("Digite o número da tarefa concluida")) - 1
        if 0 <= indice < len(tarefas):
            tarefas[indice] = f"✅ {tarefas[indice]}"
            print("Tarefa marcada como concluída!")
        else:
            print("Índice inválido.")
    elif opcao == 4:
        indice = int(input("Digite o número da tarefa a ser removida: ")) - 1
        if 0 <= indice < len(tarefas):
            tarefas.pop(indice)
            print("Tarefa removida!")
        else:
            print("Índice inválido")
    elif opcao == 5:
        print("Saindo...")
        break
    else:
        print("Opção invalida")

