from flask import Flask, jsonify, request
from flask_restful import Resource, Api
from flask_restful import reqparse
from flask_ngrok import run_with_ngrok

import get_target as gt
import contents_print
import client

app = Flask(__name__)
api = Api(app)
run_with_ngrok(app)

class Utterance_from_user(Resource):
    def post(self):
        db = client.ClientDb()
        reqparser = reqparse.RequestParser()
        data = request.get_json()
        '''
        aa = data['action']['parameters']['aa']['value']
        ###
        
        reqparser.add_argument("input_word", type=str)
        # parser.add_argument('user_name', type=str)
        # parser.add_argument('password', type=str)
        args = reqparser.parse_args()
        input_word = args['action']['parameters']["input_word"]['value'].split(',')
        
        ###
        
        target_page_n = gt.get_target_page(aa)
        t_name = str(target_page_n) + "_data"
        contents = db.select_all(t_name)
        result = contents_print.find_contents(contents,aa)
        '''
        print(data)
        result = 'No'
        return {'result': result}


api.add_resource(Utterance_from_user, '/utter_from_user')

if __name__ == '__main__':
    app.run()

###