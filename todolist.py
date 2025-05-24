import json
import os

caminho = os.path.join(os.path.dirname(__file__), 'todolist.json')

def so_aceita_int(string):
    while True:
        try:
            valor = int(input(string))
        except ValueError:
            print('ERRO, tipo de dado inválido!')
        else:
            return valor
        
    

def retornar_lista():
    with open(caminho, 'r') as file:
            lista = json.load(file)

    if len(lista) == 0:
         
         return 'A lista de tarefas está vazia'
    else:

        lista_str = ''

        for i,dc in enumerate(lista):       
                completed = 'X' if dc["completed"] else ' '
                string = f'{i+1}° {dc["name"]} [{completed}]\n'
                lista_str += string

        return lista_str

def marca_desmarca(key):
    key -= 1
    with open(caminho, 'r') as file:
        lista = json.load(file)
    
    if len(lista) == 0:
        return 'ERRO'
    elif key+1 <= 0:
        return 'ERRO'
    else:
        for i,dc in enumerate(lista):
            if i == key:
                dc["completed"] = not dc["completed"]

        with open(caminho, 'w') as file:
            json.dump(lista,file, indent=2)

def apagar(key):
    with open(caminho, 'r') as file:
        lista = json.load(file)

    if len(lista) < key or len(lista) == 0 or key <= 0:
        return 'ERRO'
    else:
        del lista[key-1]

        with open(caminho, 'w') as file:
            json.dump(lista,file, indent=2)

def criar(name):
    with open(caminho, 'r') as file:
        lista = json.load(file)

    dc = {"name": name,"completed": False}
    lista.append(dc)

    with open(caminho, 'w') as file:
            json.dump(lista,file, indent=2)
    

while True:
    
    controle = so_aceita_int(60*'='+'\n1 para ver a lista\n2 para marcar/desmarcar alguma tarefa como concluída\n3 para adicionar ou remover uma nova tarefa\n4 para sair\n'+'='*60+'\n')

    if controle == 4:
        print('Encerrando programa...')
        break

    elif controle == 1:
        print(retornar_lista())
    
    elif controle == 2:
        if retornar_lista() == 'A lista de tarefas está vazia':
                 print('ERRO, a lista está vazia!')
        else:
            print(retornar_lista())

            mudar_tarefa = so_aceita_int('Insira o número da tarefa que deseja mudar: ')

            marca_desmarca(mudar_tarefa)

    elif controle == 3:
        criar_apagar = so_aceita_int('Deseja criar[1] ou apagar[2]: ')
        if criar_apagar == 1:
            nome = input('Insira o nome da tarefa: ')
            criar(nome)

        elif criar_apagar == 2:
            if retornar_lista() == 'A lista de tarefas está vazia':
                 print('ERRO, a lista está vazia!')
            else:
                print(retornar_lista())
                index = so_aceita_int('Insira o valor que deseja apagar: ')
                apagar(index)
        else:
            print('Valor inválido!')
    else:
        print('Valor inválido!')