from ..funções import *

def arqExiste(arq):
    try:
        a = open(arq, 'rt')
    except:
        return False
    else:
        return True
def criar(arq):
    try:
        a = open(arq, 'wt+')
    except:
        print('falha ao criar arquivo')
    else:
        print('arquivo criado com sucesso')

def exbirarq(arq):
    try:
        a = open(arq, 'r')
    except:
        print('falha ao ler arquivo')
    else:
        cabecalho('Exibindo Tarefas ')
        print(a.read())
        a.close()
        linha()

def adicionar(arq,tarefa):
    try:
        a = open(arq, 'at')
    except:
        print('erro ao adicionar tarefa')
    else:
        a.write(f'\n{tarefa}\n')

def excluir(arq, remover, novo=''):
    try:
        a = open(arq, 'r')
        conteudo = a.read()
        a.close()
    except:
        print('erro ao ler')
    else:
        novo_conteudo = conteudo.replace(remover, novo)
        try:
            a = open(arq, 'w')
        except:
            print('erro ao excluir')
        else:
            a.write(novo_conteudo)
            a.close()

