from flask import Flask, jsonify, request
from flask_cors import CORS
import json

from persistence import *

app = Flask("Multivix")
CORS(app)


@app.route("/api/capitalIntelectual", methods=["GET"])
def get():
    tarefas = carregar()
    return jsonify(tarefas)

@app.route("/api/capitalIntelectual", methods=["POST"])
def post():
    tarefa = request.get_json()
    salvar(tarefa)

    resultado = { "message": 'Registro salvo com sucesso'}
    return jsonify({"result": resultado})


app.run(debug=True)
