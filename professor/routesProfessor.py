from flask import Blueprint, request, jsonify
from .modelProfessor import (
    ProfessorNaoEncontrado,
    ProfessorJaExiste,
    model_create_professor,
    model_get_professor,
    model_get_professor_id,
    model_update_professor,
    model_delete_professor
)

professor = Blueprint('professor', __name__)

@professor.route('/professor', methods = ['POST'])
def create_professor():
    dados = request.json
    try:
        professor = model_create_professor(dados)
        return jsonify(professor), 201
    except ProfessorJaExiste:
        return jsonify({'erro': 'ID já existe!'}), 400
    except Exception as e:
        return jsonify({'erro': f'Erro inesperado ao criar professor: {str(e)}'}), 500

    
@professor.route('/professor', methods = ['GET'])
def get_professor():
    try: 
        professores = model_get_professor()
        return jsonify(professores)
    except Exception as e:
        return jsonify({'erro': f'Erro inesperado ao listar professores: {str(e)}'}), 500


@professor.route('/professor/<int:idprofessor>', methods = ['GET'])
def get_professor_id(idprofessor):
    try:
        professor = model_get_professor_id(idprofessor)
        return jsonify(professor)
    except ProfessorNaoEncontrado:
        return jsonify({'erro': 'Professor não encontrado!'}), 404
    except Exception as e:
        return jsonify({'erro': f'Erro inesperado ao buscar professor: {str(e)}'}), 500


@professor.route('/professor/<int:idprofessor>', methods = ['PUT'])
def update_professor(idprofessor):
    try:
        dados = request.json
        professor_atualizado = model_update_professor(idprofessor, dados)
        return jsonify(professor_atualizado)
    except ProfessorNaoEncontrado: 
        return jsonify({'erro': 'Professor não encontrado!'}), 404
    except Exception as e:
        return jsonify({'erro': f'Erro inesperado ao atualizar professor: {str(e)}'}), 500
    
    
@professor.route('/professor/<int:idprofessor>', methods=['DELETE'])
def delete_professor(idprofessor):
    try:
        model_delete_professor(idprofessor)
        return jsonify({'mensagem': 'Professor deletado com sucesso!'}), 200
    except ProfessorNaoEncontrado:
        return jsonify({'erro': 'Professor não encontrado!'}), 404
    except Exception as e:
        return jsonify({'erro': f'Erro inesperado ao deletar professor: {str(e)}'}), 500
    