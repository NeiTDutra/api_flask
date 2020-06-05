from flask import Flask, request
from flask_restful import Resource, Api
from skils import Skil
import json

app = Flask(__name__)
api = Api(app)

desenvolvedores = [
    {'nome': 'Nei',
     'skils': ['Python', 'Flask']},
    {'nome': 'Thomassin',
     'skils': ['Python', 'Django']},
    {'nome': 'Dutra',
     'skils': ['PHP', 'Slim']}
]

class Desenvolvedor(Resource):
    def get(self, id):
        dev = desenvolvedores[id]
        return dev

    def put(self, id):
        dados = json.loads(request.data)
        desenvolvedores[id] = dados
        return dados

    def delete(self, id):
        desenvolvedores.pop(id)
        return {'status':'sucesso', 'mensagem':'Registro escluido'}

class ListaDesenvolvedores(Resource):
    def get(self):
        return desenvolvedores

    def post(self):
        dados = json.loads(request.data)
        posicao = len(desenvolvedores)
        dados[id] = posicao
        desenvolvedores.append(dados)
        return desenvolvedores[posicao]


api.add_resource(Desenvolvedor, '/dev/<int:id>/')
api.add_resource(ListaDesenvolvedores, '/dev/')
api.add_resource(Skil, '/skil/')

if __name__ == '__main__':
    app.run(debug=True)