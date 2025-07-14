from flask import Blueprint, request, jsonify, Response
from datetime import datetime
from backend import db
from backend.models.tasks import Tasks
from flasgger import swag_from

import locale
locale.setlocale(locale.LC_TIME, 'pt_BR.UTF-8')

tasks_bp = Blueprint('tasks',__name__, url_prefix='/tasks')

@tasks_bp.route('/', methods=['POST'])
@swag_from({
    'tags': ['Tarefas'],
    'operationId': 'criarTarefa',
    'parameters': [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'properties': {
                    'titulo': {
                        'type': 'string',
                        'example': 'Comprar pão'
                    },
                    'descricao': {
                        'type': 'string',
                        'example': 'Ir à padaria e comprar 2 pães'
                    }
                },
                'required': ['titulo', 'descricao']
            }
        }
    ],
    'responses': {
        201: {
            'description': 'Tarefa criada com sucesso.'
        },
        400: {
            'description': 'Erro ao criar tarefa.'
        }
    }
})
def criar__tarefa():
    data = request.get_json()

    data_criacao = datetime.strptime(data.get("data_criacao"), "%Y-%m-%d %H:%M") if data.get("data_criacao") else datetime.utcnow()
    
    nova_tarefa = Tasks(
        titulo = data["titulo"],
        descricao = data["descricao"],
        data_criacao = data_criacao
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
    """
    Retorna a lista de todas as tarefas cadastradas.
    ---
    operationId: listarTarefas
    tags:
      - Tarefas
    responses:
      200:
        description: Lista de tarefas retornada com sucesso.
      400:
        description: Erro ao consultar tarefas.
    """

    try:
        dados_tarefas = Tasks.query.all()
        tarefas = []

        for dado in dados_tarefas:
            tarefas.append({
                "id": dado.id,
                "titulo": dado.titulo,
                "descricao": dado.descricao,
                "data_criacao": dado.data_criacao.strftime("%A, %d de %B às %H:%M").capitalize().replace("-feira", "") if dado.data_criacao else None,
                "data_conclusao": dado.data_conclusao.strftime("%A, %d de %B às %H:%M").capitalize().replace("-feira", "") if dado.data_conclusao else None,
                "concluida":dado.concluida,
            })
        return jsonify(tarefas)
    
    except:
        return jsonify(
            {"mensagem":"Erro ao consultar tarefas"}
            ), 400

@tasks_bp.route('/<int:id>', methods=['GET'])
def listar_tarefa_especifica(id):
    """
    Retorna os dados de uma tarefa específica pelo ID.
    ---
    operationId: listarTarefaPorId
    tags:
      - Tarefas
    parameters:
      - name: id
        in: path
        required: true
        schema:
          type: integer
    responses:
      200:
        description: Tarefa encontrada com sucesso.
      404:
        description: Tarefa não encontrada.
      400:
        description: Erro ao consultar tarefa.
    """
    
    try:
        dados_tarefa = Tasks.query.get(id)

        if (dados_tarefa) is None:
            return jsonify ({"mensagem":"Tarefa não encontrada"}), 404
        
        tarefa = {
                "id": dados_tarefa.id,
                "titulo": dados_tarefa.titulo,
                "descricao": dados_tarefa.descricao,
                "data_criacao": dados_tarefa.data_criacao.strftime("%A, %d de %B às %H:%M").capitalize().replace("-feira", "") if dados_tarefa.data_criacao else None,
                "data_conclusao": dados_tarefa.data_conclusao.strftime("%A, %d de %B às %H:%M").capitalize().replace("-feira", "") if dados_tarefa.data_criacao else None,
                "concluida":dados_tarefa.concluida
        }

        return jsonify (tarefa), 201

    except:
        return jsonify ({"mensagem": "Erro ao consultar tarefa"}), 400

@tasks_bp.route('/<int:id>', methods=['PUT'])
@swag_from({
    'tags': ['Tarefas'],
    'operationId': 'editarTarefa',
    'parameters': [
        {
            'name': 'id',
            'in': 'path',
            'type': 'integer',
            'required': True,
            'description': 'ID da tarefa a ser editada'
        },
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'properties': {
                    'titulo': {
                        'type': 'string',
                        'example': 'Atualizar título'
                    },
                    'descricao': {
                        'type': 'string',
                        'example': 'Atualizar descrição'
                    },
                    'concluida': {
                        'type': 'boolean',
                        'example': True
                    }
                },
                'required': ['titulo', 'descricao']
            }
        }
    ],
    'responses': {
        200: {
            'description': 'Tarefa atualizada com sucesso.'
        },
        400: {
            'description': 'Erro ao atualizar tarefa.'
        },
        404: {
            'description': 'Tarefa não encontrada.'
        }
    }
})
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
    """
    Exclui uma tarefa específica com base no ID.
    ---
    operationId: excluirTarefa
    tags:
      - Tarefas
    parameters:
      - name: id
        in: path
        required: true
        schema:
          type: integer
    responses:
      200:
        description: Tarefa excluída com sucesso.
      400:
        description: Erro ao tentar excluir a tarefa.
      404:
        description: Tarefa não encontrada.
    """

    tarefa = Tasks.query.get(id)
    
    if not tarefa:
        return jsonify({"mensagem": "Tarefa não encontrada"})
    
    try:
        db.session.delete(tarefa)
        db.session.commit()
        return jsonify({"mensagem": "Tarefa excluída com sucesso."})
    
    except:
        db.session.rollback()
        return jsonify({"mensagem": "Erro ao tentar excluir a tarefa."})