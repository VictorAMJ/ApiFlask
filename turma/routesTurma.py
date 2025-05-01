from flask import Blueprint, request, jsonify
from config import db
from .modelTurma import TurmaNãoEncontrada, model_create_turma, model_get_turma, model_get_turma_por_id, model_update_turma, model_delete_turma

turma = Blueprint('turma', __name__)

@turma.route('/turma', methods=["POST"])
def create_turma():
    dados = request.json
    try:
        print(f"dados coletados: {dados}")
        resposta, status_code = model_create_turma(dados)
        return jsonify(resposta), status_code
    except Exception as e:
        return jsonify({'erro': f'Erro inesperado ao criar turma: {str(e)}'}), 500
    
    
@turma.route('/turma', methods =["GET"])
def get_turma():
    try:
        turma = model_get_turma()
        return jsonify(turma)
    except Exception as e:
        return jsonify({'erro': f'Erro inesperado ao buscar turma: {str(e)}'}), 500

    
@turma.route("/turma/<int:idturma>", methods=["GET"])
def get_turma_por_id(idturma):
    try:
        turma = model_get_turma_por_id(idturma)
        return jsonify(turma)
    except TurmaNãoEncontrada:
        return jsonify({'erro':'Turma não encontrada'}), 404
    except Exception as e:
        print({'erro': f'Erro inesperado ao buscar turma: {str(e)}'}), 500
    

@turma.route("/turma/<int:idturma>", methods=["PUT"])
def update_turma(idturma):
    dados = request.json
    try:
        turma = model_update_turma(idturma, dados)
        if not turma:
            return jsonify({'erro':'Turma não encontrada'}), 404
        model_update_turma(idturma, dados)
        return jsonify(turma), 200
    except TurmaNãoEncontrada:
        return({'erro':'Turma não encontrada'}), 404
    except Exception as e:
        return jsonify({'erro': f'Erro inesperado ao atualizar turma: {str(e)}'}), 500
    

@turma.route("/turma/<int:idturma>", methods=["DELETE"])
def delete_turma(idturma):
    try:
        model_delete_turma(idturma)
        return jsonify({'mensagem': 'Turma deletada com sucesso!'}), 200
    except TurmaNãoEncontrada:
        return jsonify({'erro':'Turma não encontrada'}), 404
    except Exception as e:
        return jsonify({'erro': f'Erro inesperado ao deletar turma: {str(e)}'}), 500

