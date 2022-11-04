from flask import Flask, jsonify, request
from flask_cors import CORS
import json

app = Flask("Multivix")
CORS(app)


@app.route("/api/tasks", methods=["GET"])
def get():
    return "Olá"


app.run(debug=True)
