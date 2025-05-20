from datetime import datetime, date
from config import db


class Professor(db.Model):
    __tablename__ = "professor"

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50), nullable=False)
    idade = db.Column(db.String(10), nullable=False)
    materia = db.Column(db.String(50), nullable=False)
    observacoes = db.Column(db.String(100), nullable=False)

    def __init__(self, nome, idade, materia, observacoes):
        self.nome = nome
        self.idade = idade
        self.materia = materia
        self.observacoes = observacoes
    
    def transforma_em_dic(self):
        return{
            'id': self.id,
            'nome': self.nome,
            'idade': self.idade,
            'materia': self.materia,
            'observacoes': self.observacoes
        }

class ProfessorNaoEncontrado(Exception):
    pass

def model_create_professor(dados):
    novo_professor = Professor(
        nome= dados["nome"],
        idade = dados["idade"],
        materia= dados["materia"],
        observacoes= dados["observacoes"]
    )

    db.session.add(novo_professor)
    db.session.commit()
    return {"mensagem":"Professor adicionado com sucesso!"}, 201
        

def model_get_professor():
    professores = Professor.query.all()
    print(professores)
    return [professor.transforma_em_dic() for professor in professores]


def model_get_professor_id(idprofessor):
    professor = Professor.query.get(idprofessor)
    if not professor:
        raise ProfessorNaoEncontrado("Professor não encontrado!")
    return professor.transforma_em_dic()
    
        
def model_update_professor(idprofessor, dados_novos):
    professor = Professor.query.get(idprofessor)
    if not professor:
        raise ProfessorNaoEncontrado("Professor não encontrado.")
    
    professor.nome = dados_novos["nome"]
    professor.idade = dados_novos["idade"]
    professor.materia = dados_novos["materia"]
    professor.observacoes = dados_novos["observacoes"]

    db.session.commit()
    return {
        "id": professor.id,
        "nome": professor.nome,
        "idade": professor.idade,
        "materia": professor.materia,
        "observacoes": professor.observacoes
    }


def model_delete_professor(idProfessor):
    professor = Professor.query.get(idProfessor)
    if not professor:
        raise ProfessorNaoEncontrado("Professor não encontrado!")
    
    db.session.delete(professor)
    db.session.commit()
