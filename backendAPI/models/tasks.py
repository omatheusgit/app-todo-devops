from backendAPI import db
from sqlalchemy import func

class Tasks(db.model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(30), nullable=False)
    descricao = db.Column(db.String(200), nullable=False)
    data_criacao = db.Column(db.DateTime(timezone=True),server_default=func.now())
    data_conclusao = db.Column(db.DateTime(timezone=True))
    concluida = db.Column(db.Bolean, default=False, nullable=False)

