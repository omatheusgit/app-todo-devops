from flask import Blueprint, jsonify
from backendAPI import app

app_bp = Blueprint('app',__name__)

@app_bp.route('/ping', methods=['GET'])
def verifica_api():
    '''Função para verificar se a API responde'''
    return jsonify(
        data = {"api":"pong"}
        )

if __name__ == '__main__':
    app.run(debug=True)