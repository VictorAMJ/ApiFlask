from flask import Flask, jsonify, request

app = Flask(__name__)


#PROFESSOR:
dicionarioProfessor = {
    "professores": [{
        "id": 1,
        "nome":"Caio",
        "idade": 27,
        "materia": "Desenvolvimento de APIs e Microsserviços",
        "observacoes": "Professor legal"
    }]
}

#ALUNO:
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

#TURMA:
dicionarioTurma = {
    "turma" : [{
        "id": 1,
        "descricao": "nenhuma",
        "professor_id": 1, 
        "ativo": True
    }]
}



#CRIAR PROFESSOR:
@app.route("/professor", methods=["POST"])
def create_professor():
    dados = request.json
    dici_professores = dicionarioProfessor["professores"]
    for professor in dici_professores:
        if professor["id"] == dados["id"]:
            return jsonify({"erro": "ID já existe."}), 400
        
    professor = {
        "id": dados["id"],
        "nome": dados["nome"],
        "idade": dados["idade"],
        "materia": dados["materia"],
        "observacoes": dados["observacoes"]
    }

    dicionarioProfessor["professores"].append(professor)
    return jsonify(professor), 201


#LER PROFESSOR
@app.route("/professor", methods=["GET"])
def get_professor():
    dados = dicionarioProfessor["professores"]
    return jsonify(dados)


#LER PROFESSOR ID
@app.route("/professor/<int:idprofessor>", methods=["GET"])
def get_professor_id(idprofessor):
    for professor in dicionarioProfessor["professores"]:
        if professor["id"] == idprofessor:
            return jsonify(professor)
    return jsonify({"erro": "Professor não encontrado!"}), 404


#ATUALIZAR PROFESSOR
@app.route("/professor/<int:idprofessor>", methods=["PUT"])
def update_professor(idprofessor):
    dici_professor = dicionarioProfessor["professores"]
    
    for professor in dici_professor:
        if professor["id"] == idprofessor:
            dadosprofessor = request.json

            professor["id"] = dadosprofessor["id"]
            professor["nome"] = dadosprofessor["nome"]
            professor["idade"] = dadosprofessor["idade"]
            professor["materia"] = dadosprofessor["materia"]
            professor["observacoes"] = dadosprofessor["observacoes"]

            return jsonify(professor)
    
    return jsonify({"erro": "Professor não encontrado"}), 404


#DELETAR PROFESSOR
@app.route("/professor/<int:idProfessor>", methods=["DELETE"])
def delete_professor(idProfessor):
    dici_professores = dicionarioProfessor["professores"]
    for professor in dici_professores:
        if professor["id"] == idProfessor:
            dici_professores.remove(professor)
            return jsonify({"mensagem": "Professor deletado com sucesso!"}), 200
    
    return jsonify({"erro": "Professor não encontrado."}), 404



#CRIAR ALUNO
@app.route("/aluno", methods=["POST"])
def create_aluno():
    dadosAluno = request.json
    dici_aluno = dicionarioAluno["aluno"]

    for aluno in dici_aluno:
        if aluno["id"] == dadosAluno["id"]:
            return jsonify({"erro": "ID já existe."}), 400
        
    turma_existe = False
    for turma in dicionarioTurma["turma"]:
        if turma["id"] == dadosAluno["turma_id"]:
            turma_existe = True
            break

    if not turma_existe:
        return jsonify({"erro": "Turma não encontrada"}), 400
        
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
    return jsonify(aluno), 201


#LER ALUNO
@app.route("/aluno", methods=["GET"])
def get_aluno():
    dadosAlunos = dicionarioAluno["aluno"]
    return jsonify(dadosAlunos)


#LER ALUNO ID
@app.route("/aluno/<int:idAluno>", methods=["GET"])
def get_aluno_por_id(idAluno):
    for aluno in dicionarioAluno["aluno"]:
        if aluno["id"] == idAluno:
            return jsonify(aluno)
    return jsonify({"erro": "Aluno não encontrado!"}), 404


#ATUALIZAR ALUNO
@app.route("/aluno/<int:idAluno>", methods=["PUT"])
def update_aluno(idAluno):
    dici_alunos = dicionarioAluno["aluno"]
    for aluno in dici_alunos:
        if aluno["id"] == idAluno:
            dadosAluno = request.json
            aluno["id"] = dadosAluno["id"]
            aluno["nome"] = dadosAluno["nome"]
            aluno["idade"] = dadosAluno["idade"]
            aluno["turma_id"] = dadosAluno["turma_id"]
            aluno["data_nascimento"] = dadosAluno["data_nascimento"]
            aluno["nota_primeiro_semestre"] = dadosAluno["nota_primeiro_semestre"]
            aluno["nota_segundo_semestre"] = dadosAluno["nota_segundo_semestre"]
            aluno["media_final"] = dadosAluno["media_final"]
            return jsonify(aluno)
    
    return jsonify({"erro": "Aluno não encontrado!"}), 404


#DELETAR ALUNO
@app.route("/aluno/<int:idAluno>", methods=["DELETE"])
def delete_aluno(idAluno):
    dici_aluno = dicionarioAluno["aluno"]
    for aluno in dici_aluno:
        if aluno["id"] == idAluno:
            dici_aluno.remove(aluno)
            return jsonify({"mensagem": "Aluno deletado com sucesso!"}), 200
    
    return jsonify({"erro": "Aluno não encontrado!"}), 404



#CRIAR TURMA
@app.route("/turma", methods=["POST"])
def create_turma():
    dadosTurma = request.json
    dici_turma = dicionarioTurma["turma"]

    professor_existe = False
    for professor in dicionarioProfessor["professores"]:
        if professor["id"] == dadosTurma["professor_id"]:
            professor_existe = True
            break

    if not professor_existe:
        return jsonify({"erro": "Professor não encontrado"}), 400


    for turma in dici_turma:
        if turma["id"] == dadosTurma["id"]:
            return jsonify({"erro": "ID já existente."}), 400
        
    turma = {
        "id": dadosTurma["id"],
        "descricao":dadosTurma["descricao"],
        "professor_id":dadosTurma["professor_id"],
        "ativo":dadosTurma["ativo"]
    }

    dicionarioTurma["turma"].append(turma)
    return jsonify(turma), 201


#LER TURMA
@app.route("/turma", methods=["GET"])
def get_turma():
    dadosTurma = dicionarioTurma["turma"]
    return jsonify(dadosTurma)


#LER TURMA ID
@app.route("/turma/<int:idturma>", methods=["GET"])
def get_turma_por_id(idturma):
    for turma in dicionarioTurma["turma"]:
        if turma["id"] == idturma:
            return jsonify(turma)
    return jsonify({"erro": "Turma não encontrada"}), 404


#ATUALIZAR TURMA
@app.route("/turma/<int:idturma>", methods=["PUT"])
def update_turma(idturma):
    dici_turma = dicionarioTurma["turma"]
    for turma in dici_turma:
        if turma["id"] == idturma:
            dadosturma = request.json

            professor_existe = False
            for prof in dicionarioProfessor["professores"]:
                if prof["id"] == dadosturma["professor_id"]:
                    professor_existe = True
                    break

            if not professor_existe:
                return jsonify({"erro": "Professor não encontrado"}), 400
            
            turma["descricao"] = dadosturma["descricao"]
            turma["professor_id"] = dadosturma["professor_id"]
            turma["ativo"] = dadosturma["ativo"]
            return jsonify(turma)
        
    return jsonify({"erro": "Turma não encontrada."}), 404


#DELETAR TURMA
@app.route("/turma/<int:idturma>", methods=["DELETE"])
def delete_turma(idturma):
    dici_turma = dicionarioTurma["turma"]
    for turma in dici_turma:
        if turma["id"] == idturma:
            dici_turma.remove(turma)
            return jsonify({"mensagem": "Turma deletado com sucesso."}), 200
    
    return jsonify({"erro": "Turma não encontrada."}), 404



if __name__=="__main__":
    app.run(debug=True)
