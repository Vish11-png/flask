from flask import Flask, jsonify
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

nameage = {"abc":{"age":19, "gender": "male"},
        "xyz":{"age": 20, "gender": "female"}}

vid = {1:{"name":"vid 1", "likes":10, "views":10000},
    2:{"name":"vid 2", "likes":20, "views":20000},
    3:{"name":"vid 3", "likes":30, "views":30000}}

class HelloWorld(Resource):
    def get(self):
        return {'data':'HelloWorld'}
    def post(self):
        return {'data': 'Post method used'}

class multi(Resource):
    def get(self, num):
        return  {'result': num*10}

class names(Resource):
    def get(self, name):
        return nameage[name]

class vidinfo(Resource):
    def get(self, vid_id):
        return vid[vid_id]

class numst(Resource):
    def get(self, n, st):
        return {"number":n, 
                "string":st}

api.add_resource(HelloWorld, '/')
api.add_resource(multi,'/<int:num>')
api.add_resource(names, '/name/<string:name>')
api.add_resource(vidinfo, '/video/<int:vid_id>')
api.add_resource(numst, '/number/<int:n>/<string:st>')

if __name__=="__main__":
    app.run(debug=True)