from flask import Flask, jsonify, request, redirect, url_for,session, render_template
from flask_cors import CORS
import os

from update_stats import  insert_stats
from get_teams import  get_teams
from get_teams import  get_team_list

import json
from bson import ObjectId

class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        return json.JSONEncoder.default(self, o)


# PARTE2
app = Flask(__name__)
CORS(app)


# HELLO
@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
    return response
    
@app.route('/')
def hello():

    return "Bem vindo a central de API do CyberBaska"


#DEVX

# @app.route('/api/devxcadastrar', methods=['POST'])
# def cadastrar_devx():
#     data = request.json
#     if data['ativo'] != "" :
#         AlimentarBase(data)
#         return jsonify(data)

@app.route('/api/insert_stats', methods=['GET'])
def inserir_stats():

    return insert_stats()

@app.route('/api/get_teams_list', methods=['GET'])
def get_teams_list():

    return jsonify(get_team_list())

@app.route('/api/get_team_a', methods=['POST'])
def get_team():

    team = request.json
    print(team)

    return JSONEncoder().encode(get_teams(team['TEAM_A']))

@app.route('/api/get_team_b', methods=['POST'])
def get_team_b():

    team = request.json
    print(team)

    return JSONEncoder().encode(get_teams(team['TEAM_B']))    


if __name__ == '__main__':
    # port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=80)
