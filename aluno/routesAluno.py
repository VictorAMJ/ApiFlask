from flask import Blueprint, request, jsonify
from .modelAluno import(
    AlunoNaoEncontrado,
    AlunoJaExiste,
    model_create_aluno,
    model_get_aluno,
    model_get_aluno_por_id,
    model_update_aluno,
    model_delete_aluno
)

aluno = Blueprint('aluno', __name__)

@aluno.route("/aluno", methods=["POST"])
def create_aluno():
    dadosAluno = request.json
    try:
        aluno = model_create_aluno(dadosAluno)
        return jsonify(aluno), 201
    except AlunoJaExiste:
        return jsonify({"erro": "ID já existe"}), 400
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
    try:
        dadosAluno = request.json
        aluno_atualizado = model_update_aluno(idAluno, dadosAluno)
        return jsonify(aluno_atualizado)
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
    