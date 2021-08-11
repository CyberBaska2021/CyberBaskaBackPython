from flask import Flask, jsonify, request, redirect, url_for,session, render_template
from flask_cors import CORS
import os

from update_stats import  insert_stats

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


if __name__ == '__main__':
    # port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=80)
