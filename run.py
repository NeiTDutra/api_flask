from flask import Flask, jsonify, request
import json

app = Flask(__name__)

desenvolvedores = [
    {'nome': 'Nei',
     'skils': ['Python', 'Flask']},
    {'nome': 'Thomassin',
     'skils': ['Python', 'Django']},
    {'nome': 'Dutra',
     'skils': ['PHP', 'Slim']}
]


@app.route('/dev/<int:id>/', methods=['GET', 'PUT', 'DELETE'])
def desenvolvedor(id):
    if request.method == 'GET':
        dev = desenvolvedores[id]
        return jsonify(dev)
    elif request.method == 'PUT':
        dados = json.loads(request.data)
        desenvolvedores[id] = dados
        return jsonify(dados)
    elif request.method == 'DELETE':
        desenvolvedores.pop(id)


@app.route('/dev/new', methods=['POST', 'GET'])
def desenvolvedor_todo():
    if request.method == 'POST':
        dados = json.loads(request.data)
        desenvolvedores.append(dados)
        return jsonify({'status': 'Sucesso', 'mensagem': 'Registro inserido'})
    elif request.method == 'GET':
        return jsonify(desenvolvedores)


# @app.route('/<int:id>')
# def main_api(id):
#     return jsonify({'id': id, 'nome': 'Nike', 'profissao': 'desenvolvedor'})
#
#
# @app.route('/soma/<int:valor1>/<int:valor2>')
# def soma(valor1, valor2):
#     return jsonify({'soma': valor1 + valor2})
#
#
# @app.route('/soma_post', methods=['POST'])
# def soma_post():
#     dados = json.loads(request.data)
#     soma_total = sum(dados['valor'])
#     return jsonify({'soma_post': soma_total})


if __name__ == '__main__':
    app.run(debug=True)
