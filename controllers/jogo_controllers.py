from models.jogo_models import jogo  # Importa o modelo Carro
from db import db  # Importa a conexão com o banco de dados
import json
from flask import make_response, request

# Função para obter todos os carros
def get_jogo():
    jogo = jogo.query.all()  # Busca todos os carros no banco de dados
    response = make_response(
        json.dumps({
            'mensagem': 'Lista de jogo.',
            'dados': [jogo.json() for jogo in jogo]  # Converte os objetos de carro para JSON
        }, ensure_ascii=False, sort_keys=False)  # Mantém caracteres especiais corretamente formatados
    )
    response.headers['Content-Type'] = 'application/json'  # Define o tipo de conteúdo como JSON
    return response

# Função para obter um carro específico por ID
def get_jogo_by_id(jogo_id):
    jogo = jogo.query.get(jogo_id)  # Busca o carro pelo ID

    if jogo:  # Verifica se o carro foi encontrado
        response = make_response(
            json.dumps({
                'mensagem': 'jogo encontrado.',
                'dados': jogo.json()  # Converte os dados do carro para formato JSON
            }, ensure_ascii=False, sort_keys=False)
        )
        response.headers['Content-Type'] = 'application/json'  # Garante que o tipo da resposta seja JSON
        return response
    else:
        # Se o carro não for encontrado, retorna erro com código 404
        response = make_response(
            json.dumps({'mensagem': 'jogo não encontrado.', 'dados': {}}, ensure_ascii=False),
            404  # Código HTTP 404 para "Não encontrado"
        )
        response.headers['Content-Type'] = 'application/json'  # Define que a resposta é em JSON
        return response

# Função para criar um novo carro
def create_jogo(jogo_data):
    # Valida se todos os campos obrigatórios foram fornecidos
    if not all(key in jogo_data for key in ['titulo', 'genero', 'desenvolvedor', 'plataforma']):
        response = make_response(
            json.dumps({'mensagem': 'Dados inválidos. titulo, genero, desenvolvedor e plataforma são obrigatórios.'}, ensure_ascii=False),
            400  # Código HTTP 400 para requisição inválida
        )
        response.headers['Content-Type'] = 'application/json'  # Garante que a resposta seja em JSON
        return response
    
    # Se os dados forem válidos, cria o novo carro
    novo_jogo = jogo(     
        titulo=jogo_data['titulo'],
        genero=jogo_data['genero'],
        desenvolvedor=jogo_data['desenvolvedor'],
        plataforma=jogo_data['plataforma']
    )
    
    db.session.add(novo_jogo)  # Adiciona o novo carro ao banco de dados
    db.session.commit()  # Confirma a transação no banco

    # Resposta de sucesso com os dados do novo carro
    response = make_response(
        json.dumps({
            'mensagem': 'jogo cadastrado com sucesso.',
            'jogo': novo_jogo.json()  # Retorna os dados do carro cadastrado
        }, ensure_ascii=False, sort_keys=False)
    )
    response.headers['Content-Type'] = 'application/json'  # Define que a resposta é em JSON
    return response

    # Função para atualizar um carro por ID
def update_jogo(jogo_id, jogo_data):
    jogo = jogo.query.get(jogo_id)  # Buscar o carro pelo ID

    if not jogo:  # Se o carro não for encontrado, retorna erro
        response = make_response(
            json.dumps({'mensagem': 'jogo não encontrado.'}, ensure_ascii=False),
            404 # Código HTTP 404 para "Não encontrado"
        )
        response.headers['Content-Type'] = 'application/json'   #Garante que a resposta seja em json
        return response
    
        # valida se todos os campos obrigatorios foram fornecidos
    if not all(key in jogo_data for key in ['titulo', 'genero', 'desenvolvedor', 'plataforma']):
        response = make_response(
            json.dumps({'mensage': 'Dados invalidos. titulo, genero, desenvolvedor e plataforma são abrigatórios'}, ensure_ascii=False),
            400 # Codigo HTTP 400 para requisição invalida
        )
        response.headers['Content-Type'] = 'application/json'  #define que a resposta é em json
        return response
        
        # Atualiza os dados do carro
    jogo.titulo = jogo_data['titulo']
    jogo.genero = jogo_data['genero']
    jogo.desenvolvedor = jogo_data['desenvolvedor']
    jogo.plataforma = jogo_data['plataforma']

    db.session.commit()   #confirma a atualização no banco de dados

        # retorna a resposta com os dados do carro atualizado
    response = make_response(
        json.dumps({
            'mensagem': 'jogo atualizado com sucesso.',
            'jogo': jogo.json()
        }, ensure_ascii=False, sort_keys=False)
    )
    response.headers['Content-Type'] = 'application/json'   #Define que a resposta é em JSON
    return response