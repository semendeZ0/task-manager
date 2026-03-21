from functions import *

while True:
    print('-=' * 20)
    menu('criar lista de tarefas', 'adicionar tarefas à lista', 'verificar tarefas da lista','concluir tarefas', 'ENCERRAR PROGRAMA')
    print('-' * 20)
    try:
        user = int(input('Selecione uma opção: '))
    except ValueError:
        print('Digite apenas números inteiros, por favor.')

    if user == 1:
        criar_lista(str(input('Digite o nome da lista de tarefas: ')))

    elif user == 2:
        criar_tarefa(str(input('Digite o nome da lista em que deseja adicionar a tarefa: ')))

    elif user == 3:
        mostrar_lista(str(input('Digite a lista de tarefas que deseja olhar: ')))

    elif user == 4:
        concluir_tarefa(str(input('Digite a lista de tarefas que deseja acessar: ')))
    
    elif user == 5:
        break
    
    else:
        print('Opção inválida! Por favor, tente novamente.')
print('Encerrando o programa...')
sleep(2)