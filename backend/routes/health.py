from flask import Blueprint, jsonify

health_bp = Blueprint('health',__name__)

@health_bp.route('/ping', methods=['GET'])
def verifica_api():
    """
    Verifica se a API está ativa.
    ---
    operationId: verificarStatusAPI
    tags:
      - Healthcheck
    responses:
      200:
        description: API está respondendo corretamente.
    """

    return jsonify(
        data = {"api":"pong"}
        )