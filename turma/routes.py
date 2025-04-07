from flask import Blueprint
from .model import create_turma, get_turma, get_turma_por_id, update_turma, delete_turma

turma = Blueprint('turma', __name__)

@turma.route('/turma', methods=["GET"])
def create_turma():
    pass
    
@turma.route('/turma', methods =["GET"])
def get_turma():
    pass

@turma.route("/turma/<int:idturma>", methods=["GET"])
def get_turma_por_id():
    pass

@turma.route("/turma/<int:idturma>", methods=["PUT"])
def update_turma():
    pass

@turma.route("/turma/<int:idturma>", methods=["DELETE"])
def delete_turma():
    pass
