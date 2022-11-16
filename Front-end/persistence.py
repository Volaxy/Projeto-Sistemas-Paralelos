from flask import Flask, jsonify, request
from flask_cors import CORS
import json

from flask import jsonify


def carregar():
    with open('tarefas.json') as json_tarefa:
        return json.load(json_tarefa)

def salvar(capital_intelectual):
    capitais_intelectuais = carregar()

    file = open("tarefas.json", mode="w")
    file.write(jsonify(capital_intelectual))
