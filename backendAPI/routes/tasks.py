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
    try:
        dados_tarefa = Tasks.query.get(id)

        if (dados_tarefa) is None:
            return jsonify ({"mensagem":"Tarefa não encontrada"}), 404
        
        tarefa = {
                "id": dados_tarefa.id,
                "titulo": dados_tarefa.titulo,
                "descricao": dados_tarefa.descricao,
                "data_criacao": dados_tarefa.data_criacao,
                "data_conclusao": dados_tarefa.data_conclusao,
                "concluida":dados_tarefa.concluida
        }

        return jsonify (tarefa), 201

    except:
        return jsonify ({"mensagem": "Erro ao consultar tarefa"}), 400

@tasks_bp.route('/<int:id>', methods=['PUT'])
def editar_tarefa_especifica(id):
    
    tarefa = Tasks.query.get(id)
    if tarefa is None:
        return jsonify ({"mensagem":"Tarefa não encontrada"}), 404
    
    data = request.get_json()
    if not data:
        return jsonify ({"mensagem": "Dados do JSON inválidos."})

    try:
        campos_permitidos = ['titulo', 'descricao', 'concluida']

        for chave, valor in data.items():

            if not chave in campos_permitidos:
                return jsonify({"mensagem":"Campo imutavel foi escolhido"})

            elif chave in campos_permitidos and hasattr(tarefa, chave):
                setattr(tarefa, chave, valor)

        db.session.commit()

        return jsonify({"mensagem":"Tarefa atualiza com sucesso."})
    
    except:
        db.session.rollback()
        return jsonify({"mensagem": "Erro ao tentar atualizar a tarefa."})
    
@tasks_bp.route('/<int:id>', methods=['DELETE'])
def deletar_tarefa_especifica(id):
    return