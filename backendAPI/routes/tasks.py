from flask import Blueprint, request, jsonify, Response

tasks_bp = Blueprint('tasks',__name__, url_prefix='/tasks')

@tasks_bp.route('/', methods=['GET'])
def listar_tarefas():
    data = {'messagem':'OK'}
    return jsonify (data)

@tasks_bp.route('/', methods=['POST'])
def criar__tarefa():
    dados_tarefa = {
        "titulo": titulo,
        "descricao": descricao,
        "concluida": concluida,
        "data_criacao": data_criacao
    }
    if Response.status_code == 200:
        return jsonify (
            data = {"mensagem": "Tarefa criada com sucesso."}
            ), 200
    else:
        return jsonify(
            data = {"messagem":"Erro ao criar tarefa"}
        )
        

@tasks_bp.route('/<int:id>', methods=['GET'])
def listar_tarefa_especifica(id):
    dados_tarefa = {
        "id": id,
        "titulo": titulo,
        "descricao": descricao,
        "concluida": concluida,
        "data_criacao": data_criacao
    }
    if Response.status_code == 200:
        return jsonify(
            data = {"mensagem": "Tarefa editada com sucesso."}
            ), 200
    else:
        return jsonify(
            data = {"messagem": "Erro ao buscar tarefa"}
            )

@tasks_bp.route('/<int:id>', methods=['PUT'])
def editar_tarefa_especifica(id):
    if Response.status_code == 200:
        data = {}
        return jsonify(data)

@tasks_bp.route('/<int:id>', methods=['DELETE'])
def deletar_tarefa_especifica(id):
    return