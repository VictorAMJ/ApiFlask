from Turma.modelTurma import Turma
from datetime import datetime, date
from config import db

class Aluno(db.Model):
    __tablename__ = "aluno"

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    data_nascimento = db.Column(db.Date, nullable=False)
    idade = db.Column(db.Integer, nullable=False)
    nota_primeiro_semestre = db.Column(db.Float, nullable=False)
    nota_segundo_semestre = db.Column(db.Float, nullable=False)
    media_final = db.Column(db.Float, nullable=False)
    turma_id = db.Column(db.Integer, db.ForeignKey("turma.id"), nullable=False)

    def __init__(self, nome, data_nascimento, nota_primeiro_semestre, nota_segundo_semestre, media_final, turma_id):
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.nota_primeiro_semestre = nota_primeiro_semestre
        self.nota_segundo_semestre = nota_segundo_semestre
        self.media_final = media_final
        self.turma_id = turma_id
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
            'nota_primeiro_semestre': self.nota_primeiro_semestre,
            'nota_segundo_semestre': self.nota_segundo_semestre,
            'media_final': self.media_final,
            'turma_id': self.turma_id
        }

class AlunoNaoEncontrado(Exception):
    pass

class TurmaNãoEncontrada(Exception):
    pass

def model_create_aluno(dadosAluno):
    turma = Turma.query.get(dadosAluno['turma_id'])
    if (turma is None):
        raise TurmaNãoEncontrada('Turma não encontrada')
    
    novo_aluno = Aluno(
        nome= dadosAluno["nome"],
        data_nascimento= datetime.strptime(dadosAluno['data_nascimento'], "%Y-%m-%d").date(),
        nota_primeiro_semestre= float(dadosAluno["nota_primeiro_semestre"]),
        nota_segundo_semestre= float(dadosAluno["nota_segundo_semestre"]),
        turma_id= int(dadosAluno["turma_id"]),
        media_final= (float(dadosAluno["nota_primeiro_semestre"]) + float(dadosAluno["nota_segundo_semestre"]))/ 2
    )

    db.session.add(novo_aluno)
    db.session.commit()
    return{"mensagem":"Aluno adicionado com sucesso!"}, 201


def model_get_aluno():
    alunos = Aluno.query.all()
    print(alunos)
    return [aluno.transforma_em_dic() for aluno in alunos]


def model_get_aluno_por_id(idAluno):
    aluno = Aluno.query.get(idAluno)
    if not aluno:
        raise AlunoNaoEncontrado('Aluno não Encontrado')
    return aluno.transforma_em_dic()
   

def model_update_aluno(idAluno, dadosAluno):
    aluno = Aluno.query.get(idAluno)
    if not aluno:
        raise AlunoNaoEncontrado('Aluno não Encontrado')
    
    turma = Turma.query.get(dadosAluno['turma_id'])
    if (turma is None):
        raise TurmaNãoEncontrada('Turma não encontrada')
    
    aluno.nome = dadosAluno["nome"]
    aluno.turma_id = dadosAluno["turma_id"]
    aluno.data_nascimento = datetime.strptime(dadosAluno["data_nascimento"], "%Y-%m-%d").date()
    aluno.nota_primeiro_semestre = dadosAluno["nota_primeiro_semestre"]
    aluno.nota_segundo_semestre = dadosAluno["nota_segundo_semestre"]
    aluno.media_final = (float(dadosAluno["nota_primeiro_semestre"]) + float(dadosAluno["nota_segundo_semestre"]))/ 2
    aluno.idade = aluno.calcular_idade()

    db.session.commit()
    return {
        'id': aluno.id,
        'nome': aluno.nome,
        'data_nascimento': aluno.data_nascimento.isoformat(),
        'idade': aluno.idade,
        'nota_primeiro_semestre': aluno.nota_primeiro_semestre,
        'nota_segundo_semestre': aluno.nota_segundo_semestre,
        'media_final': aluno.media_final,
        'turma_id': aluno.turma_id
    }
    

def model_delete_aluno(idAluno):
    aluno = Aluno.query.get(idAluno)
    if not aluno:
        raise AlunoNaoEncontrado('Aluno não encontrado')
    
    db.session.delete(aluno)
    db.session.commit()
