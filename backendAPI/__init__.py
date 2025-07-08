import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
from flasgger import Swagger

db = SQLAlchemy()

def create_app():
    load_dotenv()
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLALCHEMY_DATABASE_URI')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    swagger_config = {
        "headers": [],
        "specs": [
            {
                "endpoint": 'apispec',
                "route": '/docs.json',
                "rule_filter": lambda rule: True,
                "model_filter": lambda tag: True,
            }
        ],
        "static_url_path": "/flasgger_static",
        "swagger_ui": True,
        "specs_route": "/docs/"
    }

    swagger_template = {
        "swagger": "2.0",
        "info": {
            "title": "To-Do API",
            "description": "Essa API é o backend do meu aplicativo de tarefas To-Do.",
            "version": "1.0"
        },
        "basePath": "/",
        "schemes": ["http"]
    }

    Swagger(app, config=swagger_config, template=swagger_template)

    # Importações internas e registro dos blueprints
    from .routes.tasks import tasks_bp
    from .routes.health import health_bp
    app.register_blueprint(tasks_bp)
    app.register_blueprint(health_bp)

    return app