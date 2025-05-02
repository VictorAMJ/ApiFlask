from professor.modelProfessor import Professor
from config import db

class Turma(db.Model):
    __tablename__ = "turma"

    id = db.Column(db.Integer, primary_key=True)
    descricao = db.Column(db.String(50), nullable=False)
    ativo = db.Column(db.Boolean, nullable=False)
    professor_id = db.Column(db.Integer, db.ForeignKey("professor.id"), nullable= False)

    def __init__(self, descricao, ativo, professor_id):
        self.descricao = descricao
        self.ativo = ativo
        self.professor_id = professor_id

    def transforma_em_dic(self):
        return{
            'id':self.id,
            'descricao': self.descricao,
            'ativo': self.ativo,
            'professor_id': self.professor_id
        }

class TurmaNãoEncontrada(Exception):
    pass

class ProfessorNãoEncontrado(Exception):
    pass

def model_create_turma(dadosTurma):
    professor = Professor.query.get(dadosTurma['professor_id'])
    if (professor is None):
        raise ProfessorNãoEncontrado('Professor não encontrado')
    
    nova_turma = Turma(
        descricao= dadosTurma['descricao'],
        ativo= dadosTurma['ativo'],
        professor_id= int(dadosTurma['professor_id'])
    )

    db.session.add(nova_turma)
    db.session.commit()
    return{"mensagem":"Turma adicionada com sucesso!"}, 201


def model_get_turma():
    turmas = Turma.query.all()
    print(turmas)
    return [turma.transforma_em_dic() for turma in turmas]


def model_get_turma_por_id(idturma):
    turma = Turma.query.get(idturma)
    if not turma:
        raise TurmaNãoEncontrada('Turma não encontrada')
    return turma.transforma_em_dic()
    

def model_update_turma(idturma, dadosTurma):
    turma = Turma.query.get(idturma)
    if not turma:
        raise TurmaNãoEncontrada('Turma não encontrada')
    
    professor = Professor.query.get(dadosTurma['professor_id'])
    if (professor is None):
        raise ProfessorNãoEncontrado('Professor não encontrado')
    
    turma.descricao = dadosTurma["descricao"]
    turma.professor_id = dadosTurma["professor_id"]
    turma.ativo = dadosTurma["ativo"]

    db.session.commit()
    return{
        'id': turma.id,
        'descricao': turma.descricao,
        'ativo': turma.ativo,
        'professor_id': turma.professor_id
    }


def model_delete_turma(idturma):
    turma = Turma.query.get(idturma)
    if not turma:
        raise TurmaNãoEncontrada('Turma não encontrada')
    
    db.session.delete(turma)
    db.session.commit()
    