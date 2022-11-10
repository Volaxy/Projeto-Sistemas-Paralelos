
import json

def carregar():
    with open('tarefas.json') as json_tarefa:
        return json.load(json_tarefa)

def salvar(tarefa):
    tarefas = carregar()
    tarefas.append(tarefa)

    with open('tarefas.json', 'w') as json_tarefa:
        return json.dump(tarefas, json_tarefa)



app.run(debug=True)
