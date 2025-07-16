import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
from flasgger import Swagger
from .swagger_config import swagger_config, swagger_template

db = SQLAlchemy()

def create_app():
    load_dotenv()
    app = Flask(__name__)
    db_path = os.getenv('SQLITE_PATH')
    db_abspath = os.path.abspath(db_path)
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_abspath}'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    Swagger(app, config=swagger_config, template=swagger_template)

    # Importações internas e registro dos blueprints
    from .routes.tasks import tasks_bp
    from .routes.health import health_bp
    app.register_blueprint(tasks_bp)
    app.register_blueprint(health_bp)

    return app