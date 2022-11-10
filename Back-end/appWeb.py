from flask import Flask, jsonify, request
from flask_cors import CORS
import json

from persistence import *

app = Flask("Multivix")
CORS(app)


@app.route("/api/tasks", methods=["GET"])
def get():
    tarefas = carregar()
    return jsonify(tarefas)

@app.route("/api/tasks", methods=["POST"])
def post():
    tarefa = request.get_json()

    resultado = { "message": 'Registro salvo com sucesso'}
    return jsonify(resultado)


app.run(debug=True)
