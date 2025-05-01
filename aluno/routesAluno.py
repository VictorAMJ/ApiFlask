from flask import Blueprint, request, jsonify
from datetime import datetime
from config import db
from .modelAluno import(
    AlunoNaoEncontrado,
    model_create_aluno,
    model_get_aluno,
    model_get_aluno_por_id,
    model_update_aluno,
    model_delete_aluno
)

aluno = Blueprint('aluno', __name__)

@aluno.route("/aluno", methods=["POST"])
def create_aluno():
    try:
        dadosAluno = request.json
        print(f"dados coletados: {dadosAluno}")
        resposta, status_code = model_create_aluno(dadosAluno)
        return jsonify(resposta), status_code
    except Exception as e:
        return jsonify({"erro": f"Erro indesperado ao criar aluno: {str(e)}"}), 500
    
    
@aluno.route("/aluno", methods=["GET"])
def get_aluno():
    try:
        aluno = model_get_aluno()
        return jsonify(aluno)
    except Exception as e:
        return jsonify({"erro": f"Erro inesperado ao listar alunos: {str(e)}"}), 500


@aluno.route("/aluno/<int:idAluno>", methods=["GET"])
def get_aluno_por_id(idAluno):
    try:
        aluno = model_get_aluno_por_id(idAluno)
        return jsonify(aluno)
    except AlunoNaoEncontrado:
        return jsonify({"erro": "Aluno não encontrado!"}), 404
    except Exception as e:
        return jsonify({"erro": f"Erro inesperado ao buscar alunos: {str(e)}"}), 500


@aluno.route("/aluno/<int:idAluno>", methods=["PUT"])
def update_aluno(idAluno):
    dadosAluno = request.json
    try:
        aluno_atualizado = model_update_aluno(idAluno, dadosAluno)
        if not aluno_atualizado:
            return jsonify({'erro':'Aluno não encontrado'}), 404
        model_update_aluno(idAluno, dadosAluno)
        return jsonify(dadosAluno), 200
    except AlunoNaoEncontrado:
        return jsonify({"erro": "Aluno não encontrado!"}), 404
    except Exception as e:
        return jsonify({"erro": f"Erro inesperado ao atualizar alunos: {str(e)}"}), 500


@aluno.route("/aluno/<int:idAluno>", methods=["DELETE"])
def delete_aluno(idAluno):
    try:
        model_delete_aluno(idAluno)
        return jsonify({"mensagem": "Aluno deletado com sucesso!"}), 200
    except AlunoNaoEncontrado:
        return jsonify({"mensagem": "Aluno não encontrado!"}), 404
    except Exception as e:
        return jsonify({"erro": f"Erro inesperado ao deletar alunos: {str(e)}"}), 500
