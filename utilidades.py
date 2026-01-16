def linhas():
    print('-' * 30)

def cabecalo(texto):
    linhas()
    print(f'{texto:^40}')
    linhas()

def menu(opcoes):
    for indice, linhas in enumerate(opcoes):
        print(f'\033[33m{indice + 1}\033[m - \033[34m{linhas}\033[m')


def descricoes():
    print(f'{'ID':<4} {'TAREFA':<30} - {'STATUS':>12}')

