import os
from dotenv import load_dotenv
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Imports dos Blueprints
from backendAPI.routes.tasks import tasks_bp
from backendAPI.app          import app_bp

load_dotenv() # carrega as .env

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLSQLALCHEMY_DATABASE_URI')
# configuração para habilitar ou desabilitar modificações de rastreamento de objetos. Reduz memoria
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Registro dos blueprints
app.register_blueprint(tasks_bp)
app.register_blueprint(app_bp)