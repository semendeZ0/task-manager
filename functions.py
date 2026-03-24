from time import sleep
import os

def criar_tarefa(nome_arquivo):
    """
    -> cria uma tarefa no arquivo escolhido.
    > nome_arquivo = o arquivo que está armazenando as informações desejadas
    se o arquivo já existir, ele funcionará sem problemas. Caso contrário, dará erro.
    """
    while True:
        while True:
                if os.path.exists(f'{nome_arquivo}.txt'):
                    tarefa = str(input('Digite a tarefa a ser adicionada: '))
                    with open(f'{nome_arquivo}.txt', 'a', encoding='utf-8') as arquivo:
                        arquivo.write(f'[ ] {tarefa}\n')
                        break     
                else:
                    print('\033[31mERRO: LISTA DE TAREFAS NÃO ENCONTRADA!\033[m\nPor favor, certifique-se de que o nome da lista está correto!')
                    sleep(1)
                    nome_arquivo = str(input('Digite o nome do arquivo novamente: '))
        
        print(f'\033[1;32mTarefa {tarefa} adicionada com sucesso!\033[m')
        while True:
            user = str(input('Deseja adicionar mais uma tarefa[S/N]? ')).upper().strip()[0]
            if user in ['S', 'N']:
                break
            else:
                print('Por favor, responda apenas S ou N!')
        if user == 'N':
            break
    

def criar_lista(titulo):
    """
    -> criar_lista gera um arquivo .txt no dispositivo, onde haverá as atividades que o usuário registrar. Se o arquivo já existir no computador, a função retornará um ERRO.
    """
    try:
        with open(f'{titulo}.txt', 'x', encoding='utf-8') as arquivo:
            pass
        print(f'\033[1;32mLista "{titulo}" criada com sucesso! ✓\033[m')
        sleep(1)
    except FileExistsError:
        print('\033[31mARQUIVO JÁ EXISTENTE\033[m. Por favor, dê um nome diferente ao arquivo, para não misturar as tarefas :)')


def concluir_tarefa(nome_arquivo):
    """
    --> Concluí uma tarefa imposta pelo usuário. 
    > nome_arquivo: Determina o arquivo que será procurado no sistema e exibido na tela.
    """
    while True:
        if os.path.exists(f'{nome_arquivo}.txt'):
            with open(f'{nome_arquivo}.txt', 'r', encoding='utf-8') as arquivo:
                linhas = arquivo.readlines()
            break
        else:
            print('Lista inexistente!')
            nome_arquivo = str(input('Digite o nome da lista novamente: '))
    while True:
        print(f'=== LISTA DE TAREFAS {nome_arquivo} ===')
        for i, linha in enumerate(linhas):
            print(f'{i + 1}. {linha}', end='')
        print()

        while True:
            try:
                numero = int(input('Qual tarefa deseja marcar como concluída? ')) - 1
                if 0 <= numero < len(linhas):
                    break
                else:
                    print('\033[31mTarefa inexistente!\033[m Por favor, insira o número exato da tarefa!')
                    sleep(1)
            except (TypeError, ValueError):
                print('\033[31mERRO: CARACTER INVÁLIDO.\033[mPor favor, digite apenas números inteiros.')
                continue
        linhas[numero] = linhas[numero].replace('[ ]', '[ \033[1;32mx\033[m ]')
        
        with open(f'{nome_arquivo}.txt', 'w', encoding='utf-8') as arquivo:
            arquivo.writelines(linhas)
        print('\033[1;32mTarefa concluída com sucesso! ✓\033[m')
        print('Meus parabéns :D')
        sleep(1)
        while True:
            confirmacao = str(input('Deseja concluir mais uma tarefa da lista[S/N]? ')).upper().strip()[0]
            if confirmacao in ['S', 'N']:
                break
            else:
                print('Responda apenas S ou N, por favor!')
        if confirmacao == 'N':
            break



def mostrar_lista(nome_arquivo):
    """
    mostra todos os itens da lista, sem poder alterar nada. Apenas exibe.
    """
    while True:
        if os.path.exists(f'{nome_arquivo}.txt'):
            with open(f'{nome_arquivo}.txt', 'r', encoding='utf-8') as arquivo:
                linhas = arquivo.readlines()
            break
        else:
            print(f'Lista inexistente!')
            nome_arquivo = str(input('Digite o nome da lista novamente: '))
    print(f'=== LISTA DE TAREFAS {nome_arquivo} ===')
    for i, linha in enumerate(linhas):
        print(f'{i + 1}. {linha}', end='')
    print()
    sleep(2)


def menu(*opções):
    """
    cria um menu na tela de acordo com a quantidade de opções postas.
    """
    for indice, nome in enumerate(opções):
        print(f'[ {indice + 1} ] - {nome}')


def excluir_lista(nome_arquivo):
    if os.path.exists(f'{nome_arquivo}.txt'):
        while True: 
            confirmacao = str(inpuT('Tem certeza que deseja excluir essa lista[S/N]? ')).upper().strip()[0]
            if confirmacao in ['S', 'N']:
                break
            else:
                print('RESPOSTA INVÁLIDA. Por favor, responda apenas S ou N.')
        if confirmacao == 'S':
            os.remove(f'{nome_arquivo}.txt')
            print(f'Lista "{nome_arquivo}" excluída com sucesso!')
        else:
            print('Operação cancelada.')
    else:
        print(f'\033[31mLISTA NÃO ENCONTRADA!\033[m')
