def linha():
    print('-' *50)

def cabecalho(msg):
    linha()
    print(msg.center(50))
    linha()

def exibirmenu(menu):
    c = 1
    for i in menu:
        print(f'{c} - {i}')
        c+=1
    linha()
    opcao = lerint('digite a opção desejada: ')
    return opcao

def lerint(num):
    while True:
        try:
            entrada = int(input(num))
        except:
            print('Número invalido')
        else:
            return entrada