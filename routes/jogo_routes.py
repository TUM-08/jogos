from flask import Blueprint, request  
from controllers.jogo_controllers import get_jogo, create_jogo, get_jogo_by_id, update_jogo

# Define um Blueprint para as rotas de "Carro"
jogo_routes = Blueprint('jogo_routes', __name__)  

# Rota para listar todos os carros (GET)
@jogo_routes.route('/jogo', methods=['GET'])
def jogo_get():
    return get_jogo()

# Rota para buscar um carro pelo ID (GET)
@jogo_routes.route('/jogo/<int:jogo_id>', methods=['GET'])
def jogo_get_by_id(jogo_id):
    return get_jogo_by_id(jogo_id)

# Rota para criar um novo carro (POST)
@jogo_routes.route('/jogo', methods=['POST'])
def jogo_post():
    return create_jogo(request.json)

@jogo_routes.route('/jogo/<int:jogo_id>', methods=['put'])
def jogo_put(jogo_id):
    jogo_data = request.json
    return update_jogo(jogo_id, jogo_data)

