#IMPORTA MODEL DE PROFESSOR


dicionarioTurma = {
    "turma" : [{
        "id": 1,
        "descricao": "nenhuma",
        "professor_id": 1, 
        "ativo": True
    }]
}

class TurmaNãoEncontrada(Exception):
    pass

class ProfessorNãoEncontrado(Exception):
    pass

class TurmaJáExiste(Exception):
    pass

def create_turma(dadosTurma):
    dici_turma = dicionarioTurma["turma"]

    professor_existe = False
    for professor in dicionarioProfessor["professores"]:
        if professor["id"] == dadosTurma["professor_id"]:
            professor_existe = True
            break

    if not professor_existe:
        raise ProfessorNãoEncontrado('Professor não encontrado')

    for turma in dici_turma:
        if turma["id"] == dadosTurma["id"]:
            raise TurmaJáExiste("Essa turma com esse ID, já existe")
        
    turma = {
        "id": dadosTurma["id"],
        "descricao":dadosTurma["descricao"],
        "professor_id":dadosTurma["professor_id"],
        "ativo":dadosTurma["ativo"]
    }

    dicionarioTurma["turma"].append(turma)


def get_turma():
    return  dicionarioTurma["turma"]


def get_turma_por_id(idturma):
    for turma in dicionarioTurma["turma"]:
        if turma["id"] == idturma:
            return turma
    raise TurmaNãoEncontrada('Turma não encontrada')
    

def update_turma(idturma, dadosturma):
    dici_turma = dicionarioTurma["turma"]
    for turma in dici_turma:
        if turma["id"] == idturma:

            professor_existe = False
            for prof in dicionarioProfessor["professores"]:
                if prof["id"] == dadosturma["professor_id"]:
                    professor_existe = True
                    break

            if not professor_existe:
                raise ProfessorNãoEncontrado('Professor não encontrado')
            
            turma["descricao"] = dadosturma["descricao"]
            turma["professor_id"] = dadosturma["professor_id"]
            turma["ativo"] = dadosturma["ativo"]
            return turma
    
    raise TurmaNãoEncontrada('Turma não encontrada')


def delete_turma(idturma):
    dici_turma = dicionarioTurma["turma"]
    for turma in dici_turma:
        if turma["id"] == idturma:
            dici_turma.remove(turma)
    
    raise TurmaNãoEncontrada('Turma não encontrada')
    