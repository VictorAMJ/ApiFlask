dicionarioProfessor = {
    "professores": [{
        "id": 1,
        "nome":"Caio",
        "idade": 27,
        "materia": "Desenvolvimento de APIs e Microsserviços",
        "observacoes": "Professor legal"
    }]
}

class ProfessorNaoEncontrado(Exception):
    pass

class ProfessorJaExiste(Exception):
    pass



def model_create_professor(dados):
    
    dici_professores = dicionarioProfessor["professores"]
    for professor in dici_professores:
        if professor["id"] == dados["id"]:
            raise ProfessorJaExiste('ID já existe!')
        
    professor = {
        "id": dados["id"],
        "nome": dados["nome"],
        "idade": dados["idade"],
        "materia": dados["materia"],
        "observacoes": dados["observacoes"]
    }

    dicionarioProfessor["professores"].append(professor)
    return professor


def model_get_professor():
    dados = dicionarioProfessor["professores"]
    return dados


def model_get_professor_id(idprofessor):
    for professor in dicionarioProfessor["professores"]:
        if professor["id"] == idprofessor:
            return professor
    raise ProfessorNaoEncontrado("Professor não encontrado!")
    

def model_update_professor(idprofessor, dadosprofessor):
    dici_professor = dicionarioProfessor["professores"]
    
    for professor in dici_professor:
        if professor["id"] == idprofessor:

            professor["id"] = dadosprofessor["id"]
            professor["nome"] = dadosprofessor["nome"]
            professor["idade"] = dadosprofessor["idade"]
            professor["materia"] = dadosprofessor["materia"]
            professor["observacoes"] = dadosprofessor["observacoes"]

            return professor
    
    raise ProfessorNaoEncontrado("Professor não encontrado.")


def model_delete_professor(idProfessor):
    dici_professores = dicionarioProfessor["professores"]
    for professor in dici_professores:
        if professor["id"] == idProfessor:
            dici_professores.remove(professor)
            return
    
    raise ProfessorNaoEncontrado("Professor não encontrado!")

