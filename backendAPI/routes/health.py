from flask import Blueprint, jsonify

health_bp = Blueprint('health',__name__)

@health_bp.route('/ping', methods=['GET'])
def verifica_api():
    '''Função para verificar se a API responde'''
    return jsonify(
        data = {"api":"pong"}
        )