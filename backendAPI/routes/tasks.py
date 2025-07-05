from flask import Blueprint, request, jsonify

tasks_bp = Blueprint('tasks',__name__, url_prefix='/tasks')

@tasks_bp.route('/', methods=['GET'])
def listar_tarefas():
    return '{"message":"OK"})'

@tasks_bp.route('/', methods=['POST'])
def criar__tarefa():
    return

@tasks_bp.route('/<int:id>', methods=['GET'])
def listar_tarefa_especifica(id):
    return {
        "id": id,
        "titulo": titulo,
        "descricao": descricao,
        "concluida": concluida,
        "data_criacao": data_criacao
    }

@tasks_bp.route('/<int:id>', methods=['PUT'])
def editar_tarefa_especifica(id):
    return

@tasks_bp.route('/<int:id>', methods=['DELETE'])
def deletar_tarefa_especifica(id):
    return