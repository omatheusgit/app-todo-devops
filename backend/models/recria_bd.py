from backend import db, create_app

# Para recriar o banco de dados, executar: 
# python -m backend.models.recria_bd
app = create_app()

with app.app_context():
    db.drop_all()
    db.create_all()