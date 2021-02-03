from flask import Flask, request
from flask_restful import Resource, Api
import json
app = Flask(__name__)
api = Api(app)

desenvolvedores = [
    {
        'id': '0',
        'nome': 'Raphael',
        'habilidades': ['Python', 'Flask']
    },
    {
        'id': '1',
        'nome': 'Fernando',
        'habilidades': ['Java', 'Spring']
    }
]


class Desenvolvedor(Resource):
    def get(self, id):
        try:
            response = desenvolvedores[id]
        except IndexError:
            response = {'error': 'Index Error'}
        except Exception:
            response = {'error': 'Global error'}
        return response

    def put(self, id):
        dados = json.loads(request.data)
        desenvolvedores[id] = dados
        return dados

    def delete(self, id):
        desenvolvedores.pop(id)
        return {'ok': 'Registro excluido'}


class ListaDesenvolvedores(Resource):
    def get(self):
        return desenvolvedores

    def post(self):
        dados = json.loads(request.data)
        posicao = len(desenvolvedores)
        dados['id'] = posicao
        desenvolvedores.append(dados)
        return desenvolvedores[posicao]


api.add_resource(Desenvolvedor, '/dev/<int:id>')
api.add_resource(ListaDesenvolvedores, '/dev/')

if __name__ == '__main__':
    app.run(debug=True)
