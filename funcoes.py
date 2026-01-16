from pathlib import Path
import utilidades

tarefas = Path(r'TO DO List\To-Do-List-em-Python--CLI-\tarefas.txt')

def checar_arquivo():
    if not tarefas.exists():
        tarefas.open('w').close()
        print(f'Arquivo {tarefas.name} criado com sucesso!')
    else:
        print(f'O arquivo {tarefas.name} já existe')


def adicionar_tarefa(tarefa):
    checar_arquivo()

    novo_id = 1
    status = 'pendente'
    
    with tarefas.open('r',encoding='utf-8') as arquivo:
        for linhas in arquivo:
            linhas = linhas.strip()
            if linhas != '':
                novo_id += 1

        with tarefas.open('a', encoding='utf-8') as arquivo:
            arquivo.write(f'{novo_id};{tarefa.capitalize()};{status}\n')


def listar_tarefas():
    vazio = True
    #abre o arquivo para leitura
    with tarefas.open('r', encoding='utf-8') as arquivo:
        # Varre o arquivo e pula linhas vazias
        if not vazio:
            utilidades.descricoes()

        for linhas in arquivo:
            linhas = linhas.strip()
            if linhas == '':
                continue

            # Transforma o arquivo em lista e imprime
            vazio = False    
            dados = linhas.split(';')
            status = dados[2].strip()
            

            if vazio:
                print('Arquivo vazio')
            else:
                
                cor = '\033[31m' if status == 'pendente' else '\033[32m'
                print(f'\033[33m{dados[0]:<4}\033[m {dados[1]:<30} - {cor}{status:>12}\033[m')


def marcar_concluida(id_tarefa):
    vazio = True
    linhas_atualizadas = []
    encontrou = False
    # Abre o arquivo para leitura 
    with tarefas.open('r', encoding='utf-8') as arquivo:
        for linhas in arquivo:
            linhas = linhas.strip()
            # Checagem se o arquivo for vazio ou se for igual ao ID passado não gravar
            if linhas == '':
                continue
            
            vazio = False
            dados = linhas.split(';')
            id_atual = dados[0]
            descricao = dados[1]
            status = dados[2].strip()

            if str(id_tarefa) == id_atual:
                if status == 'concluída':
                    print('A tarefa já está com status concluída')
                    return
                else:
                    status = 'concluída'
                    encontrou = True
            linhas_atualizadas.append(f'{id_atual};{descricao};{status}\n')

        if vazio:
            print('\033[31mLista vazia\033[m')
            return
        
        if not encontrou:
            print(f'\033[31mTarefa não encontrada\033[m')
            return

    with tarefas.open('w', encoding='utf-8') as arquivo:
        for linha in linhas_atualizadas:
            arquivo.write(linha)    

    print(f'Tarefa marcada como concluída')


def listar_pendentes():
    vazio = True
  
    encontrou = False
    # Abre o arquivo para leitura 
    with tarefas.open('r', encoding='utf-8') as arquivo:
        for linhas in arquivo:
            linhas = linhas.strip()
            # Checagem se o arquivo for vazio ou se for igual ao ID passado não gravar
            if linhas == '':
                continue
            
            vazio = False
            dados = linhas.split(';')
            id_atual = dados[0]
            descricao = dados[1]
            status = dados[2].strip()
            if status == 'pendente':
                print(f'\033[33m{id_atual:<4}\033[m {descricao:<30} - \033[31m{status:>12}\033[m')
                encontrou = True
        if vazio:
            print('\033[31mNenhuma tarefa encontrada.\033[m')
            return
        if not encontrou:
            print('\033[31mNenhuma tarefa com status pendente.\033[m')
        


def listar_concluidas():
    vazio = True
  
    encontrou = False
    # Abre o arquivo para leitura 
    with tarefas.open('r', encoding='utf-8') as arquivo:
        for linhas in arquivo:
            linhas = linhas.strip()
            # Checagem se o arquivo for vazio ou se for igual ao ID passado não gravar
            if linhas == '':
                continue
            
            vazio = False
            dados = linhas.split(';')
            id_atual = dados[0]
            descricao = dados[1]
            status = dados[2].strip()
            if status == 'concluída':
                print(f'\033[33m{id_atual:<4}\033[m {descricao:<30} - \033[32m{status:>12}\033[m')
                encontrou = True
        if vazio:
            print('\033[31mNenhuma tarefa encontrada.\033[m')
            return
        if not encontrou:
            print('\033[31mNenhuma tarefa com status concluída.\033[m')
            
           
           
    




            

        
    
   
            
            
            

    
    

