from backendAPI import db, app

# Para recriar o banco de dados, executar: 
# python -m backendAPI.models.bd
with app.app_context():
    db.drop_all()
    db.create_all()