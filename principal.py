from biblioteca.arqdef import *
from biblioteca.funções import *
arq = 'tarefas.txt'
if arqExiste(arq) == True:
    print('arquivo exite')
else:
    print('arquivo não existe')
    criar(arq)

while True:
    resp = exibirmenu(['Adicionar Tarefa', 'Listar Tarefas', 'Remover Tarefa', 'Sair do Sistema de Tarefas'])
    if resp == 1:
        cabecalho('Adicionar Tarefa')
        tarefa = input('digite a tarefa que deseja adicionar: ').upper()
        adicionar(arq,tarefa)
    elif resp == 2:
        cabecalho('Listar Tarefa')
        exbirarq(arq)
    elif resp == 3:
        cabecalho('Remover Tarefas')
        while True:
            escolha = lerint('deseja excluir ou substituir? 1 para excluir e 2 para sbstituir: ')
            if escolha > 0 and escolha < 3:
                novo = ''
                break
            else:
                print('erro,digite entre 1 e 2')
        if escolha == 1:
            remover = input('digite a tarefa que deseja remover: ').upper()
        elif escolha == 2:
            remover = input('digite a tarefa que deseja remover: ').upper()
            novo = input('digite a nova tarefa: ').upper()
        excluir(arq, remover, novo)
    elif resp == 4:
        cabecalho('Saindo')
        break
    else:
        cabecalho('Digite um número dentro das opções do menu')
