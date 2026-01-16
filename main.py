import funcoes
import utilidades



while True:
    utilidades.cabecalo('\033[7mMenu\033[m')
    utilidades.menu(['Adicionar tarefa', 'Listar todas', 'Listar pendentes', 'Listar Concluídas', 'Marcar como concluída (por ID)', 'Sair'])
    try:
        opcao = int(input('Digite uma opção: '))
    except ValueError:
        print('Digite um número válido')
        continue

    if opcao == 1:
        
        tarefa = input('Qual tarefa deseja adicionar? ')
        if tarefa == '':
            print('A tarefa não pode ser vazia')
            continue
        funcoes.adicionar_tarefa(tarefa)

    if opcao == 2:
        funcoes.listar_tarefas()
    
    if opcao == 3:
        funcoes.listar_pendentes()

    if opcao == 4:
        funcoes.listar_concluidas()

    if opcao == 5:
        funcoes.marcar_concluida()

    if opcao == 6:
        print('Saindo...')
        break
    
    

    

