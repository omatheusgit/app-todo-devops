from flask import Flask

# Imports dos Blueprints
from backendAPI.routes.tasks import tasks_bp

app = Flask(__name__)

# Registro dos blueprints
app.register_blueprint(tasks_bp)

@app.route('/ping', methods=['GET'])
def verifica_api():
    '''Função para uma rota de teste de integridade da API'''
    return '{"message":"OK"})'

