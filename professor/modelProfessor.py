from datetime import datetime, date
from config import db


class Professor(db.Model):
    __tablename__ = "professor"

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50), nullable=False)
    data_nascimento = db.Column(db.Date, nullable=False)
    idade = db.Column(db.Integer, nullable=False)
    materia = db.Column(db.String, nullable=False)
    observacoes = db.Column(db.String, nullable=False)

    def __init__(self, nome, data_nascimento, materia, observacoes):
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.materia = materia
        self.observacoes = observacoes
        self.idade = self.calcular_idade()

    def calcular_idade(self):
        today = date.today()
        return today.year - self.data_nascimento.year - ((today.month, today.day)< (self.data_nascimento.month, self.data_nascimento.day))
    
    def transforma_em_dic(self):
        return{
            'id': self.id,
            'nome': self.nome,
            'data_nascimento': self.data_nascimento.isoformat(),
            'idade': self.idade,
            'materia': self.materia,
            'observacoes': self.observacoes
        }

class ProfessorNaoEncontrado(Exception):
    pass

def model_create_professor(dados):
    novo_professor = Professor(
        nome= dados["nome"],
        data_nascimento= datetime.strptime(dados['data_nascimento'], "%Y-%m-%d").date(),
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
    professor.data_nascimento = datetime.strptime(dados_novos["data_nascimento"], "%Y-%m-%d").date()
    professor.materia = dados_novos["materia"]
    professor.observacoes = dados_novos["observacoes"]
    professor.idade = professor.calcular_idade()

    db.session.commit()
    return {
        "id": professor.id,
        "nome": professor.nome,
        "data_nascimento": str(professor.data_nascimento),
        "materia": professor.materia,
        "observacoes": professor.observacoes,
        "idade": professor.idade
    }


def model_delete_professor(idProfessor):
    professor = Professor.query.get(idProfessor)
    if not professor:
        raise ProfessorNaoEncontrado("Professor não encontrado!")
    
    db.session.delete(professor)
    db.session.commit()

