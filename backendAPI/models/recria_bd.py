from backendAPI import db, create_app

# Para recriar o banco de dados, executar: 
# python -m backendAPI.models.bd
app = create_app()

with app.app_context():
    db.drop_all()
    db.create_all()