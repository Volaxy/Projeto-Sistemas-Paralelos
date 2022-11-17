from flask import Flask, jsonify, request
from flask_cors import CORS
import json

from flask import jsonify


def carregar():
    with open('tarefas.json') as json_tarefa:
        return json.load(json_tarefa)

def salvar(capital_intelectual):
    with open("tarefas.json") as json_tarefa:
        data = json.load(json_tarefa)
        dados = [data]
        dados.append(capital_intelectual)

    with open("tarefas.json", "w") as json_tarefa:
        json.dump(dados, json_tarefa)
