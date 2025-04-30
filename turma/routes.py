from flask import Blueprint, request, jsonify
from .model import TurmaNãoEncontrada, ProfessorNãoEncontrado, TurmaJáExiste, create_turma, get_turma, get_turma_por_id, update_turma, delete_turma

turma = Blueprint('turma', __name__)

@turma.route('/turma', methods=["POST"])
def create_turma():
    dados = request.json
    try:
        turma = create_turma(dados)
        return jsonify(turma), 201
    except ProfessorNãoEncontrado:
        return jsonify({'erro':'Professor não encontrado'}), 400
    except TurmaJáExiste:
        return jsonify({'erro':'ID já existe!'}), 400
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")
    
@turma.route('/turma', methods =["GET"])
def get_turma():
    return jsonify(get_turma())

@turma.route("/turma/<int:idturma>", methods=["GET"])
def get_turma_por_id(idturma):
    try:
        turma = get_turma_por_id(idturma)
        return jsonify(turma)
    except TurmaNãoEncontrada:
        return jsonify({'erro':'Turma não encontrada'})
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")

@turma.route("/turma/<int:idturma>", methods=["PUT"])
def update_turma(idturma):
    dados = request.json
    try:
        update_turma(idturma, dados)
        return jsonify(get_turma_por_id(idturma))
    except TurmaNãoEncontrada:
        return({'erro':'Turma não encontrada'}), 404
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")

@turma.route("/turma/<int:idturma>", methods=["DELETE"])
def delete_turma(idturma):
    try:
        delete_turma(idturma)
        return '', 204
    except TurmaNãoEncontrada:
        return jsonify({'erro':'Turma não encontrada'})
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")
