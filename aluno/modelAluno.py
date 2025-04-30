dicionarioAluno = {
    "aluno": [{
        "id": 1,
        "nome": "Jurema",
        "idade": 43,
        "turma_id": 1,
        "data_nascimento":"15/06/1982",
        "nota_primeiro_semestre": 6.0,
        "nota_segundo_semestre": 8.0,
        "media_final": 7.0
    }]    
}

class AlunoNaoEncontrado(Exception):
    pass

class AlunoJaExiste(Exception):
    pass


def model_create_aluno(dadosAluno):
    dici_aluno = dicionarioAluno["aluno"]
    for aluno in dici_aluno:
        if aluno["id"] == dadosAluno["id"]:
            raise AlunoJaExiste('Id já existente!')
              
    aluno = {
        "id": dadosAluno["id"],
        "nome": dadosAluno["nome"],
        "idade": dadosAluno["idade"],
        "turma_id": dadosAluno["turma_id"],
        "data_nascimento": dadosAluno["data_nascimento"],
        "nota_primeiro_semestre": dadosAluno["nota_primeiro_semestre"],
        "nota_segundo_semestre": dadosAluno["nota_segundo_semestre"],
        "media_final": dadosAluno["media_final"]
    }

    dicionarioAluno["aluno"].append(aluno)
    return aluno


def model_get_aluno():
    dadosAlunos = dicionarioAluno["aluno"]
    return dadosAlunos


def model_get_aluno_por_id(idAluno):
    for aluno in dicionarioAluno["aluno"]:
        if aluno["id"] == idAluno:
            return aluno
    raise AlunoNaoEncontrado('Aluno não Encontrado')


def model_update_aluno(idAluno, dadosAluno):
    dici_alunos = dicionarioAluno["aluno"]
    for aluno in dici_alunos:
        if aluno["id"] == idAluno:

            aluno["id"] = dadosAluno["id"]
            aluno["nome"] = dadosAluno["nome"]
            aluno["idade"] = dadosAluno["idade"]
            aluno["turma_id"] = dadosAluno["turma_id"]
            aluno["data_nascimento"] = dadosAluno["data_nascimento"]
            aluno["nota_primeiro_semestre"] = dadosAluno["nota_primeiro_semestre"]
            aluno["nota_segundo_semestre"] = dadosAluno["nota_segundo_semestre"]
            aluno["media_final"] = dadosAluno["media_final"]
            return aluno
    
    raise AlunoNaoEncontrado('Aluno não Encontrado')


def model_delete_aluno(idAluno):
    dici_aluno = dicionarioAluno["aluno"]
    for aluno in dici_aluno:
        if aluno["id"] == idAluno:
            dici_aluno.remove(aluno)
            return
    
    raise AlunoNaoEncontrado('Aluno não encontrado')
