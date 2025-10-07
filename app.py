from flask import Flask  # Importa o framework Flask para criar a aplicação web
from db import db  # Importa a instância do banco de dados SQLAlchemy
from routes.jogo_routes import jogo_routes  # Importa as rotas do módulo de carros

app = Flask(__name__) # Cria a instância da aplicação Flask

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///jogo.db' # Configura a URI do banco de dados SQLite

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Desativa o rastreamento de modificações do SQLAlchemy

db.init_app(app)  # Inicializa a aplicação com a instância do banco de dados

app.register_blueprint(jogo_routes) # Registra o blueprint das rotas de carro na aplicação Flask

# Verifica se o script está sendo executado diretamente
if __name__ == '__main__':  
    # Garante que as tabelas do banco de dados sejam criadas dentro do contexto da aplicação
    with app.app_context():  
        db.create_all()  

    app.run(debug=True)  # Inicia o servidor Flask no modo debug (útil para desenvolvimento)
