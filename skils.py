from flask_restful import Resource

skils_list = ['Python',
         'PHP',
         'Flask',
         'Django']

class Skil(Resource):
    def get(self):
        return skils_list