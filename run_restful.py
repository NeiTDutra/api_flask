from flask import Flask, request, jsonify
from flask_restful import Resource, Api
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
        return jsonify(dev)

    def put(self):
        pass

    def post(self):
        pass

    def delete(self):
        pass

api.add_resource(Desenvolvedor, '/dev/<int:id>/')

if __name__ == '__main__':
    app.run(debug=True)