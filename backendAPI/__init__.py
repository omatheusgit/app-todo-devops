import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv

db = SQLAlchemy()

def create_app():
    load_dotenv()
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLALCHEMY_DATABASE_URI')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    # Importações internas e registro dos blueprints
    from .routes.tasks import tasks_bp
    from .routes.health import health_bp
    app.register_blueprint(tasks_bp)
    app.register_blueprint(health_bp)

    return app