from flask import Blueprint, request, jsonify, Response
from backendAPI import db
from backendAPI.models.tasks import Tasks

tasks_bp = Blueprint('tasks',__name__, url_prefix='/tasks')

@tasks_bp.route('/', methods=['POST'])
def criar__tarefa():
    
    data = request.get_json()
    nova_tarefa = Tasks(
        titulo = data["titulo"],
        descricao = data["descricao"],
    )
    try:
        db.session.add(nova_tarefa)
        db.session.commit()
        return jsonify (
            {"mensagem": "Tarefa criada com sucesso."}
            ), 201
    except:
        db.session.rollback()
        return jsonify(
            {"mensagem":"Erro ao criar tarefa"}
            ), 400

@tasks_bp.route('/', methods=['GET'])
def listar_tarefas():
    
    try:
        dados_tarefa = Tasks.query.all()

        tarefas = []
        for data in dados_tarefa:
            tarefas.append({
                "id": data.id,
                "titulo": data.titulo,
                "descricao": data.descricao,
                "data_criacao": data.data_criacao,
                "data_conclusao": data.data_conclusao,
                "concluida":data.concluida
            })
        return jsonify(tarefas)
    
    except:
        return jsonify(
            {"mensagem":"Erro ao consultar tarefas"}
            ), 400

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